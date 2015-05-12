#!/bin/bash


command="cat $1 "

for i in $(seq 1 $2)
do
command="$command | mapper.py | sort | reducer.py"
done

eval $command