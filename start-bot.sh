#!/bin/sh

mkdir -p config
touch config/token.txt
touch config/db.json
touch config/exceptions.txt
touch config/quotes.txt
touch config/swearing.txt
touch config/users.txt

./python-restarter.sh bot/main.py
