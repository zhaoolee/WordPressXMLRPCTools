#!/bin/bash

git add .
git commit -m $1
git tag $1
git push
git push --tags
