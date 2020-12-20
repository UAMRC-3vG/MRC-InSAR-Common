#!/bin/sh

reldir=`dirname $0`

cd $reldir/../docs/
sphinx-apidoc -f -o source ../mrc_insar_common/
make html

cd $reldir
