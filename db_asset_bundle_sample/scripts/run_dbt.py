# scripts/run_dbt.py
import os
import subprocess
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: run_dbt.py [build|run|test]")
        sys.exit(1)

    command = sys.argv[1]  # e.g. "build", "run", or "test"

    repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_path)

    # profiles.yml lives in repo root
    os.environ["DBT_PROFILES_DIR"] = repo_path

    # which target? default to prod in Databricks
    target = os.getenv("DBT_TARGET", "dev")

    dbt_cmd = ["dbt", command, "--target", target]
    print("Running:", " ".join(dbt_cmd))

    subprocess.check_call(dbt_cmd)

if __name__ == "__main__":
    main()