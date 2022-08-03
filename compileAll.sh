#!/bin/bash
set -e

for f in basic wArray wModule; do
    echo $f
    cd $f
    build_fortran.sh 
    cd ..
done

