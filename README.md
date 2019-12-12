# artifact-upload

## Description

Upload job artifact (directory or file)

## Inputs

- `FLOWCI_JOB_ARTIFACT_PATH` (required): ex: {path}/a.jar;{dir};{dir}/b.zip

## How to use it

```yml
#  Example that togeher with git clone, maven-test plugin

envs:
  FLOWCI_GIT_URL: "https://github.com/FlowCI/spring-petclinic-sample.git"
  FLOWCI_GIT_BRANCH: "master"
  FLOWCI_GIT_REPO: "spring-petclinic"

steps:
  - name: clone
    plugin: 'gitclone'
    allow_failure: false

  - name: run unit test
    plugin: 'maven-test'

  - name: package
    plugin: 'maven-package'
```