# pyPaloBacker
Short script to backup the running config of a Panorama instance. Targeted for Panorama but will work with a normal NGFW...

# Running
This can be run using a unix / linux box daily with cron... (crontab) or Task Scheduler on windows.

Usage
`python.exe pyPaloBacker.py`

# Requriements

* Python 3
* Pan-OS capable device (9.0.x) has only been tested

# Future

Compare most recent config to the new downloaded one and decided to keep. Daily backups can slowly add up in size, 1 year at 10MB daily will cost you 3.6GB, 10MB panorama config is fairly small...
