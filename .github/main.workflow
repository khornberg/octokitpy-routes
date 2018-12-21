workflow "New workflow" {
  on = "push"
  resolves = ["ross/python-actions/setup-py/3.7@master-1"]
}

action "ross/python-actions/setup-py/3.7@master" {
  uses = "ross/python-actions/setup-py/3.7@master"
  args = "check"
}

action "ross/python-actions/setup-py/3.7@master-1" {
  uses = "ross/python-actions/setup-py/3.7@master"
  needs = ["ross/python-actions/setup-py/3.7@master"]
  args = "sdist"
}
