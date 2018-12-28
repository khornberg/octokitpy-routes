# routes
[octokit routes from npm published to pypi](https://octokit.github.io/routes/)


This is meant to be used by other python clients. One such client is [octokitpy](https://pypi.org/project/octokitpy/)


## install

```
pip install octokitpy-routes
```

## usage

Each specification is loaded and available as a single JSON loaded Python object.

`specifications` is a dictionary keyed by each api set in octokit/routes. The value of each key is the loaded JSON of the respective `index.json`.

```
from routes import specifications
public_route_data = specifications['api.github.com']
github_enterprise_route_data = specifications['ghe-2.15']
```
