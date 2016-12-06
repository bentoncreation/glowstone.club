#!/usr/bin/env bash

curl ftp://${FTP_HOST}/TSCraft.zip --user "${FTP_USER}":"${FTP_PASSWORD}" -o ~/tmp/TSCraft.zip

unzip -o ~/tmp/TSCraft.zip -d ~/tmp/
overviewer.py --config=~/bin/overviewer_config.py
