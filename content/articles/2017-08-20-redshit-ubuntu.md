Title: Redshift: setup the color temperature of your screen according to your surroundings
Date: 2017-08-20 09:11
Category: Dev
Tags: redshift, programm

> Redshift adjusts the color temperature of your screen according to your surroundings. This may help your eyes hurt less if you are working in front of the screen at night.

This is description about software from main site. 

Earlier, I used [f.lux](https://justgetflux.com/) for Windows and I was happy with this program, but when I switched to Linux, I found out that after a month the f.lux stopped working. After I found out that there might be a problem due to my video card nVidia on Ubuntu OS ([hello from Linus](https://www.youtube.com/watch?v=_36yNWw_07g)), I immediately decided to find another program and that was [Redshift](http://jonls.dk/redshift/).

## Installation
### 1. Install program

`sudo apt-get install redshift redshift-gtk`

### 2. Setup config file
Create next file `~/.config/redshift.conf` at your $HOME directory.
Example of `redshift.conf` file you can look [here](https://github.com/jonls/redshift/blob/master/redshift.conf.sample).
If you need to find quickly your location, use [f.lux: Where am I?](https://justgetflux.com/map.html)

### 3. Starting Redshift automatically
You dont need add at startup applications command lines, just type once in your terminal `redshift-gtk` and at tray icon click to "Autostart", close programm that you started, and then you can reboot to see results.