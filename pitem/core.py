import typing


class PitemDecorator:
    def __init__(self):
        pass


def pitem(cls=None, **kwargs):
    wrapper = PitemDecorator(**kwargs)
    if cls is None:
        return wrapper
    else:
        return wrapper(cls)

class Constrain:
    def test(self, v):
        pass

class Model:
    def constrained(self, c: Constrain):
        pass



class ValuesBounded:
    def values(self):
        pass





class AnnotationModel(Model):
    pass


class AttrsModel(Model):
    pass


class MarshmalloModel(Model):
    pass


class OpenApi3Model(Model):
    pass


def fields(cls: typing.Type[Model]) -> typing.Dict[str, typing.Type[Model]]:
    pass


def composite(outer, name, inner) -> Model:
    pass


def join(models: typing.Sequence[Model]) -> Model:
    """
    Join all models into one
    :param models:
    :return:
    """
    pass


def schema(cls):
    pass


def orm(cls):
    pass


def from_openapi(yaml_str_desc) -> type:
    pass


def code(obj, target, format):
    """
    Generate code for specific target
    :param obj:
    :param target:
    :param format:
    :return:
    """


def represent(obj, target, format):
    """
    Return the representation of obj in target category, with optional format.
    Example:
        represent(str, cls, JsonLoader) will deserialize str to cls object

    :param obj:
    :param target:
    :param formatter:
    :return:
    """
    pass


def dump(encoder, obj):
    pass


def load(decoder, obj):
    pass


def dumps(encoder, obj):
    pass


def loads(decoder, obj):
    pass
