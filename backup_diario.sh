#!/bin/bash
FECHA=$(date +%d-%m-%Y)
rsync -av --link-dest=/var/tmp/Backups/$(date -d yesterday +%d-%m-%Y) /home/naia/Desktop/Seguridad /var/tmp/Backups/$FECHA
