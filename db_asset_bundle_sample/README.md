# my-dbt-bundle-demo

Minimal dbt + Databricks + Asset Bundle example.

## Local dev (DEV target)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt

dbt debug --target dev
dbt run -m example_model --target dev
dbt test -m example_model --target dev
