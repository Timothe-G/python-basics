#!/bin/bash
# The first parameter passed to this script will be used as an image version. 
# If none is passed, latest will be used as a tag.
if [ -z "${1}" ]; then
   version="latest"
else
   version="${1}"
fi


docker build -t timothega/nodejs_app:${version} . 

