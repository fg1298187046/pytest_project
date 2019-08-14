import yaml


def find_yaml_data(path):
    with open('./data/%s.yml' % path, 'rb') as f:
        return yaml.load(f)
