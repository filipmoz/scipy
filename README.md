# statistic_research

Basic statistical operations using scipy (>=1.11.0).

## Setup

```bash
pip install -r requirements.txt
```

## Run tests

```bash
pytest test_stats.py -v
```

## Mean calculation (CLI)

Read whitespace-separated numbers from **input** (stdin), compute their mean, and write the result to **output** (stdout):

```bash
echo "1 2 3 4 5" | python stats_cli.py
```

Example: `echo "1 2 3 4 5" | python stats_cli.py` prints `3.0`.
