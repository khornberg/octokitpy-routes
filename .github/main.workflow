workflow "New workflow" {
  on = "push"
  resolves = ["ross/python-actions/setup-py/3.7@master-1"]
}

action "Filters for GitHub Actions" {
  uses = "actions/bin/filter@b2bea07"
  args = "branch master"
}

action "ross/python-actions/setup-py/3.7@master" {
  uses = "ross/python-actions/setup-py/3.7@master"
  needs = ["Filters for GitHub Actions"]
  args = "check"
}

action "ross/python-actions/setup-py/3.7@master-1" {
  uses = "ross/python-actions/setup-py/3.7@master"
  needs = ["ross/python-actions/setup-py/3.7@master"]
  args = "sdist"
}
