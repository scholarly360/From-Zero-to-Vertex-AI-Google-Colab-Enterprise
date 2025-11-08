# From-Zero-to-Vertex-AI-Google-Colab-Enterprise

### Dev Setup
Use devcontainer to install ( I am using so this is easy )

### Authenticate (Create Keys in Service Account)
gcloud auth activate-service-account --key-file=service-account-key.json
(https://docs.cloud.google.com/iam/docs/keys-create-delete)

### Set your project
gcloud config set project YOUR_PROJECT_ID

### Upload notebook to GCS bucket (Bucket Name already exists)
gsutil cp my_notebook.ipynb gs://your-bucket-name/notebooks/

