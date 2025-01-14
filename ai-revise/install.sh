#!/bin/bash

PACKAGE_NAME=airevise

CFG_FILE=~/.bashrc
PACKAGE_ALIAS="alias $PACKAGE_NAME=\"python -m $PACKAGE_NAME\""

python -m pip install -r "$PACKAGE_NAME/requirements.txt"
python -m pip install "$PACKAGE_NAME/"

if ! grep -q "$PACKAGE_ALIAS" "$CFG_FILE"; then
    echo "$PACKAGE_ALIAS" >>"$CFG_FILE"
fi

echo "Installation complete!"
