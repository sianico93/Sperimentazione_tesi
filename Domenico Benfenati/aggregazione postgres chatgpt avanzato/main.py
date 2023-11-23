from query_executor import run_aggregation_query
from output_handler import write_to_csv

# Configurazione del database
database_url = "postgresql://postgres:oirad1993@localhost:5432/database4test"

# Esecuzione della query
result = run_aggregation_query(database_url)

# Scrittura dei risultati su CSV
output_file = "output.csv"
write_to_csv(result, output_file)

print(f"Query results written to {output_file}")
