#!/bin/sh

dest="data/data.json"
[ -e "$dest" ] && rm "$dest"

echo "[" >> "$dest"
comma=""
for image in img/*.png img/*.jpg; do
	echo "$comma" >> "$dest"
	echo "{\"name\": \"$image\"," >> "$dest"
	echo " \"caption\": \"\"," >> "$dest"
	echo " \"description\": \"\"}" >> "$dest"
	comma=","
done
echo "]" >> "$dest"
