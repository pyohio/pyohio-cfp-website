#!/bin/bash

# Replace links with https ones prefixed w/ 2017:

git ls-files -z | xargs -0 sed -i -e 's/ href=\"\// href=\"\{\{ URL_PREFIX \}\}\//g'
