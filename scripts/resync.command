#!/bin/bash

path=$1
db_copy_path=$2

password=$(security find-generic-password -w -s "automatedscripts" -a "$USER" -l "My Keychain Item" -D "automatedscripts-password")

echo "$password" | sudo -S cp -f "$path"/chat.db "$db_copy_path"
echo "$password" | sudo -S cp -f "$path"/chat.db-shm "$db_copy_path"
echo "$password" | sudo -S cp -f "$path"/chat.db-wal "$db_copy_path"

echo "$password" | sudo -S chmod -R +rwx "$db_copy_path"

echo "$password" | sudo -S chmod -R a+w "$db_copy_path"/*

if [ $? -eq 0 ]; then
    echo -e "\nCopy succeeded"
else
    echo -e "\nCopy failed"
fi



exit

