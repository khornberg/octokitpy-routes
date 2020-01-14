import json
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), 'routes'))


def _load_spec(spec_name):
    with open(os.path.join(__location__, f'{spec_name}'), 'r') as f:
        return json.load(f)


specs = [d.name for d in os.scandir(__location__) if d.is_file() and not d.name.endswith('js')]
specifications = {spec.replace('.json', ''): _load_spec(spec) for spec in specs}
