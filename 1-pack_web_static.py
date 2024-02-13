#!/usr/bin/python3
"""
Fabric script to create a compressed archive (tgz) from the contents of the web_static
folder in the AirBnB Clone repository.
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """
    Generates a compressed tgz archive of the web_static folder.
    
    Returns:
        str: The file path of the created archive or None on failure.
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        return None
