#!/bin/bash

NAME=keystore
PREFIX=/usr/local
CLIENT_HOME=$PREFIX/share/pyshared/$NAME

# create the directory if it doesn't exist
[[ -d $CLIENT_HOME ]] || echo "creating directory $CLIENT_HOME" && mkdir -p $CLIENT_HOME

cp keystore.py $CLIENT_HOME
cp keystore $PREFIX/bin