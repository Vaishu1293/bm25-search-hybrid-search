from utils.display import banner_workers
from workflows.bm25_workflow import run_bm25_workflow

def main() -> None:
    """Run the currently active Soul Engine Mini workflow."""
    banner_workers()
    run_bm25_workflow()

if __name__ == "__main__":
    main()