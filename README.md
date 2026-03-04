# statistic_research

Basic statistical operations using scipy (>=1.11.0).

## Setup

Create and use a virtual environment, then install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

After that, `python` and `pytest` use the venv and will find scipy.

## Run tests

```bash
pytest test_stats.py -v
```

## Stats calculation (CLI)

Read whitespace-separated numbers from **input** (stdin); compute **mean**, **sample standard deviation**, and **95% confidence interval for the mean**; write results to **output** (stdout). Needs at least 2 numbers.

```bash
echo "1 2 3 4 5 6 7" | python stats_cli.py
```

Example output:

```
mean: 4.0
std:  2.160246899469287
95% CI: [1.9339078305509308, 6.066092169449069]
```
