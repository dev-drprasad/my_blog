from contextlib import contextmanager as _contextmanager

from fabric.api import env, cd, run, prefix

env.hosts = ['reddyprasad.me']


@_contextmanager
def virtualenv():
    with prefix('source ~/envs/blog/bin/activate'):
        yield


def pull():
    env.user = 'ubuntu'
    with cd('projects'):
        with cd('my_blog'):
            run('git pull')

            with virtualenv():
                run('pip install -r requirements.txt')
                run('cd src && python manage.py collectstatic --settings=project.settings.production')
                run('cd src && python manage.py migrate')