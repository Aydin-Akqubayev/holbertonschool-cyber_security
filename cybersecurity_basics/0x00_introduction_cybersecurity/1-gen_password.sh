#!/bin/bash
cat /dev/urandom | tr -cd "a-zA-Z0-9" | head -c $1
echo 
