#! /bin/bash

# Bootstrap Sphinx
sphinx-quickstart --sep -p "bstrap" -a "FOO" -r "BAR" -l "en" \
    --ext-autodoc --no-makefile --no-batchfile --no-use-make-mode;

# Copy over the intended copy of conf.py
cp source/conf_correct.py source/conf.py;

# Generate Sphinx documentation
sphinx-apidoc -o source/ ../bstrap/;

# Add "modules" to portion of index.rst in the middle of several empty lines
tr '\n' '\f' < source/index.rst | \
    sed 's/\f\f\f\f/\f\f   modules\f\f/' | tr '\f' '\n' > source/index_new.rst;
mv source/index_new.rst source/index.rst;

# Generate Sphinx HTML documentation
sphinx-build -b html source/ build/html/;
