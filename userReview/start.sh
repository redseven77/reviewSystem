#!/bin/bash

echo "----------------UPLOADING DATA----------------------"
python3 manage.py load_data --name foods.txt
echo $?
echo "----------------STARTING SERVER----------------------"
# shellcheck disable=SC2046
nohup `python3 manage.py runserver 0.0.0.0:8000` 1>&2 nohup.out
echo $?
