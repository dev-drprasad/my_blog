from contextlib import contextmanager as _contextmanager

from fabric.api import env, cd, run, prefix
from fabric.context_managers import settings
from fabric.operations import sudo

env.hosts = ['reddyprasad.me']

django_collectstatic_prompt = 'Type \'yes\' to continue, or \'no\' to cancel: '


@_contextmanager
def virtualenv():
    with prefix('source ~/.envs/blog/bin/activate'):
        yield


def bootstrap():
    env.user = 'ubuntu'

    sudo('apt update && apt upgrade')
    sudo('apt install python-virtualenv python-pip nginx')
    sudo('pip install --upgrade pip')
    run('mkdir -p apps')
    run('mkdir -p .envs')
    with cd('.envs'):
        run('virtualenv blog')
    with cd('apps'):
        run('git clone https://github.com/dev-drprasad/my_blog.git')


def pull():
    env.user = 'ubuntu'
    with cd('apps'):
        with cd('my_blog'):
            run('git pull')

            with virtualenv():
                run('pip install --upgrade pip')
                run('pip install -r requirements.txt')
                with cd('src'):
                    run('python manage.py migrate')
                    with settings(prompts={django_collectstatic_prompt: 'yes'}):
                        run('python manage.py collectstatic --settings=project.settings.production')
