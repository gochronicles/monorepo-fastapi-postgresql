from pulumi import export
from components.database import create_database
from components.cloudrun import create_cloud_run_instance
from components.gcr import create_gcr_image


# Create resources
cloud_sql_instance, sql_instance_url = create_database()
domain_image = create_gcr_image("domain")
patient_image = create_gcr_image("patient")
domain_cloud_run = create_cloud_run_instance(
    cloud_sql_instance, sql_instance_url, domain_image.image_name
)
patient_cloud_run = create_cloud_run_instance(
    cloud_sql_instance, sql_instance_url, patient_image
)

# Export resource info
# Cloud SQL - POSTGRESQL
export("cloud_sql_instance_name", cloud_sql_instance.name)
# Domain Micro Service
export("domain_full_image", domain_image.image_name)
export("domain__base_image", domain_image.base_image_name)
# Patient Micro Service
export("patient_full_image", patient_image.image_name)
export("patient__base_image", patient_image.base_image_name)
# Cloud Run URL
export("domain_cloud_run_url", domain_cloud_run.statuses[0].url)
export("patient_cloud_run_url", patient_cloud_run.statuses[0].url)
