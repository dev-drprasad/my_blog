from contextlib import contextmanager as _contextmanager

from fabric.api import env, cd, run, prefix
from fabric.context_managers import settings

env.hosts = ['reddyprasad.me']

django_collectstatic_prompt = 'Type \'yes\' to continue, or \'no\' to cancel: '


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
                with cd('src'):
                    run('python manage.py migrate')
                    with settings(prompts={django_collectstatic_prompt: 'yes'}):
                        run('python manage.py collectstatic --settings=project.settings.production')
