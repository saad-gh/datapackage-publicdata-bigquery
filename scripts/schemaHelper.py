import os
import google.cloud.bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.dirname(os.path.abspath(__file__)) + '\\authCred.json'

# Create a BigQuery client.
bigquery_client = google.cloud.bigquery.Client()

dataset_ref = bigquery_client.dataset('samples', project='bigquery-public-data')

# This line can take any of the sample tables [gsod,github_nested,github_timeline,natality,shakespeare,trigrams,wikipedia] as its argument
table_ref = dataset_ref.table('github_nested')
table = bigquery_client.get_table(table_ref)  # API call

# View table schema
print(table.schema)