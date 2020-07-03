# artifact-upload

## Description

Upload job artifact (directory or file)

## Inputs

- `artifact.path` (optional): dirs or files to upload, for example: {path}/a.jar;{dir};{dir}/b.zip
- `artifact.pattern` (optional): the file serach pattern to find out files and upload

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

  - name: upload
    envs:
      artifact.path: '${FLOWCI_MAVEN_PKGS}' # upload packges from last step
    plugin: 'artifact-upload'
```