#!/usr/bin/python3
'''
fabric commands for server upload
'''

from datetime import datetime
from fabric.operations import local, put, run, env

env.hosts = ['35.229.102.255', '35.231.130.210']
env.user = 'ubuntu'


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


def do_deploy(archive_path):
    '''
    puts files onto server
    '''

    filename = archive_path.partition('/')[2]
    data_path = '/data/web_static/releases/' + filename.partition('.')[0]

    if put(archive_path, '/tmp/{}'.format(filename)).failed is True:
        return False

    if run('mkdir -p {}'.format(data_path)).failed is True:
        return False
    my_command = 'tar -xzf /tmp/{} -C {}'.format(filename, data_path)
    if run(my_command).failed is True:
        return False
    if run('rm /tmp/{}'.format(filename)).failed is True:
        return False
    my_command = 'mv {}/web_static/* {}'.format(data_path, data_path)
    if run(my_command).failed is True:
        return False
    if run('rm -rf {}/web_static'.format(data_path)).failed is True:
        return False
    if run('rm -rf /data/web_static/current').failed is True:
        return False
    my_command = 'ln -s {} /data/web_static/current'.format(data_path)
    if run(my_command).failed is True:
        return False

    return True
