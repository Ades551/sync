#! /usr/bin/env python3

from os import system
from os import listdir
from sys import argv
from os import path


def copy(source, target):
    files_start = listdir(source)
    files_end = listdir(target)

    for i in files_start:
        path_source = f'{source}/{i}'
        path_target = f'{target}/{i}'

        try:
            if path.isfile(path_source):
                if i not in files_end:
                    print(f'copying file {i} to {path_target}')
                    system(f'cp -r "{path_source}" "{path_target}"')
            else:
                if i not in files_end:
                    print(f'creating directory {i} in {target}')
                    system(f'mkdir "{path_target}"')
                copy(path_source, path_target)
        except PermissionError:
            print(f'Failed to copy: Permission Denied {path_source}')


def remove(source, target):
    files_start = listdir(source)
    files_end = listdir(target)

    for i in files_end:
        path_source = f'{source}/{i}'
        path_target = f'{target}/{i}'

        try:
            if path.isfile(path_target):
                if i not in files_start:
                    print(f'Removing file {path_target}')
                    system(f'rm -r "{path_target}"')
            else:
                if i not in files_start:
                    print(f'Removing directory {path_target}')
                    system(f'rm -r "{path_target}"')
                else:
                    remove(path_source, path_target)
        except PermissionError:
            print(f'Failed to copy: Permission Denied {path_target}')

source, target = list(argv)[1:]

if source[-1] == '/':
    source = source[:-1]

if target[-1] == '/':
    target = target[:-1]

copy(source, target)
remove(source, target)
