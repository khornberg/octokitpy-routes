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
from octokit_routes import specifications
public_route_data = specifications['api.github.com']
github_enterprise_route_data = specifications['ghe-2.15']

from octokit_routes import webhook_names
```

## requirements

python 3.5+ for the use of `scandir`

## changelog

### 2.5.0
Load JSON files with UTF-8 encoding for Windows

### 2.4.0
No actual changes - update deploy script

### 2.3.0
Changes the webhook npm package

### 2.2.0

[Adds webhook names](https://github.com/octokit/webhooks)

### 2.1.0

Version 27 of octokit/routes. [See the release notes for breaking changes](https://github.com/octokit/routes/releases)

### 2.0.0

Version 26 of octokit/routes. [See the release notes for breaking changes](https://github.com/octokit/routes/releases)

Change python installed location from `routes` to `octokit_routes` so as not to conflict with other packages

### 1.0.0

Version 24 of octokit/routes. [See the release notes for breaking changes](https://github.com/octokit/routes/releases)

### 0.2.0

Version 20 of octokit/routes. [See the release notes for breaking changes](https://github.com/octokit/routes/releases)

### 0.1.0

This changes the version of the routes from 16 to 19; several major versions. There are some breaking changes.

Of note, a change to v19 includes,

    Note that this version introduced the deprecation of parameters.

    number was deprecated in favor of issue_number, milestone_number, pull_number
    external_identity_guid was deprecated in favor of scim_user_id
    Ideally the library would still accept the deprecated parameters but log a deprecation message. All deprecations have a timestamp, so if you release a breaking version in future, you can bump this timestamp and ignore all deprecations older than that

[Link](https://github.com/khornberg/octokitpy-routes/pull/27#issuecomment-481837113)
