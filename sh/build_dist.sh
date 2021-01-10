#!/bin/bash
reldir=`dirname $0`
curdir=$PWD

cd $reldir/../
python setup.py sdist bdist_wheel

cd $curdir
