import os
from configparser import ConfigParser


class Config(object):

    def __init__(self, path, env, env_interpolation=False):
        self.path = os.path.expanduser(path)
        self.env = env
        if env_interpolation:
            self.c = ConfigParser(env)
        else:
            self.c = ConfigParser()
        with open(self.path) as f:
            self.c.read_file(f)

    @property
    def storage(self):
        return self.c.get('storage', 'type')

    @property
    def storage_config(self):
        return dict(self.c.items(self.storage))
