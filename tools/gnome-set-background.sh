#!/bin/bash

if [ $# -ne 1 -o "$1" == "--help" ] ; then
  echo "USAGE: $0 IMAGE_FILE"
  exit 1
fi

if [ ! -f "$1" ] ; then
  echo "ERROR: cannot read file '$1'"
  echo "USAGE: $0 IMAGE_FILE"
  exit 1
fi

# get absolute path
IMAGE_FILE=$(readlink -f "$1")

gsettings set org.gnome.desktop.background draw-background false
gsettings set org.gnome.desktop.background picture-uri file://${IMAGE_FILE}
gsettings set org.gnome.desktop.background draw-background true
