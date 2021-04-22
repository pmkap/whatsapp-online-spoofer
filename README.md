# Whatsapp Online Status Spoofer

Background: https://traced.app/2021/04/13/whatsapp-status-loophole-is-aiding-cyberstalkers/

This is an idea how to mitigate Whatsapp activity tracking by appearing online permanently, not only when using the app in the foreground.

It uses [Whatsapp Web](web.whatsapp.com) to achieve this, so it only works as long as your mobile device has internet connection.

Using this could violate the Whatsapp Terms of Service, I don't know. I would not advise to use this, it's just an idea I wanted to try. Better use another messenger without this problem.

## Requirements
* [Selenium for Python](https://selenium-python.readthedocs.io/) 
* [Xvfb](https://www.x.org/releases/X11R7.7/doc/man/man1/Xvfb.1.xhtml)
* Google Chrome or Chromium

## Usage
### Create Chrome profile with linked device
* Create a folder for the Chrome profile.
* run `./spoofer.py create_profile </path/to/folder>`
* This runs web.whatsapp.com visibly in Chrome/Chromium. Follow the instructions to link it to the mobile device. The Chrome profile is stored in the specified folder.
* This should work on any platform.

### Run
* run `./spoofer.py run </path/to/folder>` with the folder from above.
* This runs web.whatsapp.com with the previously linked device in Chrome/Chromium via [Xvfb](https://en.wikipedia.org/wiki/Xvfb). No display necessary.
