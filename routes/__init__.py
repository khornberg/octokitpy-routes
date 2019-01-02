import json
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), 'routes'))


def _load_spec(spec_name):
    with open(os.path.join(__location__, spec_name, 'index.json'), 'r') as f:
        return json.load(f)


specs = [d.name for d in os.scandir(__location__) if d.is_dir() and not d.name == '__pycache__']
specifications = {spec: _load_spec(spec) for spec in specs}
