# controller-test-lab


This repo basically serves as my automation sandbox, any kind of automation practice goes here.

Why automation? Because breaking things is fun :) 

## What's being tested at the moment
A fake controller that I want to eventually turn into a mixture of code and physical hardware with an arduino for actual inputs.

Right now the controller test for battery and input.

## Planned

Build a basic physical controller with an arduino for real inputs.

## Running the tests

Requires Python 3.12.

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

The same tests run automatically on every push through GitHub Actions.

