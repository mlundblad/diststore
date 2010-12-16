#!/bin/bash

NAME=keyserver
PREFIX=/usr/local
SERVER_HOME=$PREFIX/share/pyshared/$NAME

# create the server directory if it doesn't exist
[[ -d $SERVER_HOME ]] || echo "creating directory $SERVER_HOME" && mkdir -p $SERVER_HOME

cp keyserver.py $SERVER_HOME
cp keyserver $PREFIX/bin