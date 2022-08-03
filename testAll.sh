#!/bin/bash
set -e

for f in basic wArray wModule; do
    echo $f
    cd $f
    runTests.sh
    cd ..
done

