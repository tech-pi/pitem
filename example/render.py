import jinja2
import yaml
import sys


def load_yaml(fn):
    with open(fn, "r") as fin:
        return yaml.load(fin)


def load_template(fn):
    with open(fn, "r") as fin:
        return fin.read()


class Constrain:
    def __init__(self, min_, max_):
        self.min = min_
        self.max = max_

    @classmethod
    def from_data(cls, data):
        if data is None:
            return None
        return Constrain(data['min'], data['max'])


def type_map(s):
    return {
        "integer": "int",
    }.get(s, s)


class Field:
    def __init__(self, type_, constrain=None):
        self.type = type_map(type)
        self.constrain = constrain


class Cls:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields


def create_cls(data):
    name = list(data.keys())[0]
    fields_data = data[name]['properties']
    fields = [Field(fd, fd['type'], Constrain.from_data(
        fd.get('constrain'))) for fd in fields_data]
    return Cls(name, fields)


def render(yaml_fn, template_fn):
    t = jinja2.Template(load_template(template_fn))
    d = load_yaml(yaml_fn)
    return t.render(cls=create_cls(d))

if __name__ == "__main__":
    print(argv)
    # result = render(sys.argv[0], sys.argv[1])
