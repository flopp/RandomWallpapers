#!/bin/bash

# Set wallpaper in Gnome, Unity, etc.

# Copyright (C) 2015-2020 Florian Pigorsch <mail@florian-pigorsch.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

set -euo pipefail

if [ $# -ne 1 ] || [ "$1" == "--help" ] ; then
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
gsettings set org.gnome.desktop.background picture-uri "file://${IMAGE_FILE}"
gsettings set org.gnome.desktop.background draw-background true
