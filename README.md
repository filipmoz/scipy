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

### Descriptive (default)

One line of whitespace-separated numbers → **mean**, **sample std**, **95% CI** for the mean.

```bash
echo "1 2 3 4 5 6 7" | python stats_cli.py
```

Example output:

```
mean: 4.0
std:  2.160246899469287
95% CI: [1.9339078305509308, 6.066092169449069]
```

### One-way ANOVA (`--anova`)

**Input:** one group per line (whitespace-separated numbers). **Output:** F-statistic and p-value (test whether group means differ).

```bash
python stats_cli.py --anova <<EOF
1 2 3
4 5 6
7 8 9
EOF
```

Example output:

```
one-way ANOVA:
  F: 3.0
  p: 0.125
  (p >= 0.05: do not reject H0, no significant difference)
```
