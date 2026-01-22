#!/bin/bash
curl -i -H "Host:$1" -X POST -d $3 $2
