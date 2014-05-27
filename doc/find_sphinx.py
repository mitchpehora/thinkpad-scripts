#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2014 Martin Ueding <dev@martin-ueding.de>
# Licensed under The GNU Public License Version 2 (or later)

import os.path

def main():
    ubuntu_sphinx_build = '/usr/share/sphinx/scripts/python3/sphinx-build'

    if os.path.isfile(ubuntu_sphinx_build):
        print(ubuntu_sphinx_build)
    else:
        print('sphinx-build')

if __name__ == "__main__":
    main()