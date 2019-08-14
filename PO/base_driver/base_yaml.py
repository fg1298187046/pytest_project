import yaml
import os

path = os.path.dirname(os.path.dirname(__file__))
print(path)


def find_yaml_data(filename, key):
    with open(path + '/data/%s.yml' % filename, 'rb') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)[key]
        for i in data.values():
            yield i


find_yaml_data('yaml_data', 'data')
