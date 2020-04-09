import json
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def _load_json(path):
    with open(path, 'r') as f:
        return json.load(f)


def _load_webhook_names():
    return _load_json(os.path.join(__location__, "webhooks", "names.json"))


def _load_spec(spec_name):
    return _load_json(os.path.join(__location__, "routes", spec_name))


def _list_specs():
    return [d.name for d in os.scandir(os.path.join(__location__, "routes")) if d.is_file() and not d.name.endswith('js')]


specs = _list_specs()
specifications = {spec.replace('.json', ''): _load_spec(spec) for spec in specs}

webhook_names = _load_webhook_names()
