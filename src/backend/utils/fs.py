import os
import datetime as dt
from re import findall
from pathlib import Path

from ofacd import DirectoryStructure, Rule

from .config import FS


class UploadFiles:
  def date_by_name(
    self, src: Path, date_fmt: str = '\d{4}-\d{2}-\d{2}'
  ) -> str:
    src_date = findall(date_frm, str(src))
    if not src_date:
      src_date = [str(dt.date.today())]
    return src_date[0]

  def __call__(self, src: Path):
    file_date = ''
    pass


def setup_directory_structure():
  ds = DirectoryStructure(FS.dir_static)
  ds.add((FS.dir_upload, FS.dir_organized))
  ds.create()


def organize_uploads():
  rule = Rule(path=os.path.join(FS.dir_static, FS.dir_upload))
  rule.set_file_rules(
  )


def file_date_by_name(src: Path):
  pass


def file_date(src: Path, use_name: bool = False, date_fmt: str | None = None) -> str | None:
    """Parsing date from filename by `date_fmt` or file `ctime`

    Parameters
    ----------
    date_fmt : str, None = None
        Date format in the filename
    """
    if not use_name:
        return str(dt.datetime.utcfromtimestamp(
            src.stat().st_ctime
        ).date())

    src_date = findall(date_fmt, str(src))
    if not src_date:
        return None

    # first date
    # TODO: convert to dt.date
    return src_date[0]


def files2dt_dir(
            src: Path,
            use_name: bool = False, date_fmt: str | None = None,
            copy: bool = False
    ) -> ValueError | None:
    """Sorting files to their `date` directory

    Parameters
    ----------
    src : Path
        Source directory to sort files from
    use_name : bool = False
        Files date by filename
    date_fmt : str, None = None
        Date format in the filename
    copy : bool = False
        Flag to `copy` files or `move` (replaces the exists)
    """
    # TODO: output_fmt
    if not src.is_dir():
        raise ValueError(f"Ignored, requires a directory: {src}")

    for child in src.iterdir():
        if not child.is_file():
            # TODO: add recursion
            continue

        child_date = file_date(child, use_name=use_name, date_fmt=date_fmt)
        if child_date is None:
            print(f"Ignored, `{date_fmt = }` is not matched:", child)
            continue

        child_date = child.parent.joinpath(child_date)
        if not child_date.is_dir():
            child_date.mkdir()

        dst = child_date.joinpath(child.name)
        if not copy:
            child.rename(dst)
        else:
            dst.touch()
