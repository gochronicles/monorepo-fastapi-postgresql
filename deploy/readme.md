<!--
 Copyright (c) 2021 Go Chronicles
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

### Prerequisite Setup 

1. Setup CLI [gcloud auth](https://cloud.google.com/container-registry/docs/advanced-authentication)
1. Enable
    - Cloud SQL Admin API
    - Cloud Run API
1. For Cloud Run and GCP setup [click here](https://www.pulumi.com/blog/build-publish-containers-iac/)

### Stack Configuration 

```bash
pulumi config set db_tier db-f1-micro
pulumi config set db_name mono-db
pulumi config set bucket monorepo
pulumi config set registry monorepo
pulumi config set mode dev # dev or prod (uvicorn logging will be configured accordingly)
pulumi config set gcp:project healthy-highway-318805
pulumi config set gcp:region us-central1
pulumi config set gcp:zone us-central-1a
pulumi config set --secret db_password <your_secret_password>

pulumi up  # create all assets

pulumi destroy -y # delete all assets
```
