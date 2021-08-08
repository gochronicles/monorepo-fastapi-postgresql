<!--
 Copyright (c) 2021 Go Chronicles
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

### Stack Configuration 

```bash
pulumi config set db_tier db-f1-micro
pulumi config set db_name mono-db
pulumi config set bucket monorepo
pulumi config set gcp:project healthy-highway-318805
pulumi config set gcp:region us-central1
pulumi config set gcp:zone us-central-1a
pulumi config set --secret db_password <your_secret_password>

pulumi up  # create all assets

pulumi destroy -y # delete all assets
```