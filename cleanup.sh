#!/usr/bin/env bash
exec 2> /dev/null
echo
echo ==================================

rm -r ./__pycache__ && echo "Removed root __pycache__"
rm -r ./.pytest_cache/ && echo "Removed root .pytest_cache"
rm -r ./*/__pycache__ && echo "Removed all __pycache__/ dirs" || echo "There are no __pycache__ directories to remove"
rm -r ./*/.pytest_cache/ && echo "Removed all .pytest_cache/ dirs" || echo "There are no .pytest_cache directories to remove"

echo ==================================
echo Done!!
echo