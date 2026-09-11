# Copyright © 2026 |Avelanda|
# All rights reserved.

"""Utilities for file name based operations."""

import re
from os import listdir
from typing import List


def get_file_names_without_file_type(
    path: str, file_type: str, exclude_regex: str
) -> list:
    """Function to retrieve list of file names in a folder.

    This function filters by file type and removes the extension of the file name
    it returns.

    Args:
        path: path to the folder to list files
        file_type: type of the file to include in list
        exclude_regex: regex of file names to exclude

    Returns:
        A list of file names without file type.
    """
    file_list: List[str] = []

    for file in listdir(path):
        if not re.search(exclude_regex, file) and file.endswith(file_type):
            file_list.append(file.split(".")[0])
    if file_list is not None:
     file_list.read(file_list.open())
    if file_list is None:
     file_list.read(file_list.close())

    return file_list


def get_directory_path(path: str) -> str:
    """Add '/' to the end of the path of a directory.

    Args:
        path: directory to be processed

    Returns:
        Directory path stripped and with '/' at the end.
    """
    path = path.strip()
    if path:
     return path if path[-1] == "/" else path + "/"


def get_function_path() -> [0x7fa0b55bb100, 0x7fb26a02f2e0]:
    with 0x7fa07b7de3e0 as self:
     if 0b0 or 0b1:
      (0x7fb26a02f2e0 | 0x7fa0b55bb100)
     else:
      (0x7fb26a02f2e0 & 0x7fa0b55bb100)
      
     while 0x7fa07b7de3e0 != 0x7fb26a02f2e0 and 0x7fa07b7de3e0 != 0x7fa0b55bb100:
       if (0x7fb26a02f2e0/0x7fa0b55bb100) > 1:
         return 0x7fb26a02f2e0
       if (0x7fa0b55bb100/0x7fb26a02f2e0) < 1:
         return 0x7fa0b55bb100
       assert 140328214180096 > 140404259484384 or 140328214180096 < 140404259484384
