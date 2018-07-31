#!/usr/bin/python3
'''
generates .tgz file from web_static folder
'''

from datetime import datetime
from fabric.operations import local


def do_pack():
    '''
    generates .tgz file from web_static folder
    '''

    local('mkdir -p versions; chmod 775 versions')
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    path = 'versions/web_static_{}.tgz'.format(date)
    if local('tar cfvz {} web_static'.format(path)).succeeded is True:
        return path
    return None
