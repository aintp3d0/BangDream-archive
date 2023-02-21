# BanG Dream! Girls Band Party!
- Web UI to save images, check for `#FullCombo`, `#AllPerfect` and so on
- Storing by date and hashtags `YYYY-mm-dd/full_combo/{imgs}`

```
%block nav :: center
+-------+----------------+
| $user | $cleared_songs |
+-------+----------------+

%block body :: center

+------------+
| $song_name |
+------------+
+-------+-------------+
| $song | $statistics |
+-------+-------------+


$user
	- picture
	- name
	- description ?
	- contact ?

$cleared_songs
	- difficulties: Easy, Normal, Hard, Expert, Special
	- cleared count per $difficulties

$song_name (input : search)
	- user profile
		- cleared song
		- not cleared song
	- other user profile
		- not cleared song

$song
	- name, $difficulties (not cleared transparent) + cleared count per for all users
```

### Project Structure
```bash
$ tree . --dirsfirst
.
├── src
│   ├── backend		- backend application
│   │   └── utils	- scripts
│   └── frontend	- frontend application
├── LICENSE
└── README.md
```

#### License
AGPL v3.0
<br />
Copyright (c) 2022 Nodaa Gaji
