# Making Python Classes JSON Serializable 

This is the code for my piece [Making Python classes JSON serializable](https://thinkjrs.dev/blog/making-python-classes-JSON-serializable). 

## Get it & run it 

Grab this code and make it your own. Tests w/full coverage are included. 

### Clone the repo: 

```
git clone git@github.com:thinkjrs/demo-code.git 
``` 

### Build your environment 

As you know, you shouldn't use your system Python to develop and should use an environment. To get going simply run: 

```
pipenv install --dev 
``` 

> ℹ If you don't have Pipenv installed you can run `pip install --user pipenv` or follow the directions for your system [here](https://pipenv.pypa.io/en/latest/install/). 

Now jump into your environment: 

```
pipenv shell 
``` 

### Hack on it 

This directory contains just two substantitive files, i.e.

- `some_data_structure.py`: module containing `SomeDataStructure` and `SomeDataStructureEncoder` classes as outlined in the article, and
- `test_some_data_structure`: a [`pytest`](https://docs.pytest.org) test suite with 100% coverage.

### Other goodies 

This contains a `pyproject.toml` with basic pytest defaults we use @ [Tincre](https://tincre.com). To run
tests and get a nice terminal coverage printout simply run `pytest` after you've activated your virtual environment, 
as above.

## Contributions 

If you find a mistake or means for improvement please open a PR or file an issue herein. 

A huge thanks and much ❤ in advance!
