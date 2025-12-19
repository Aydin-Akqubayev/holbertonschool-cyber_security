#!/bin/bash
cat /dev/random | tr -cd a-zA-Z0-9 | head -c $1
