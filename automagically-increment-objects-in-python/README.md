# Automagically Increment Objects in Python

This is the code for my piece [Automagically Increment Objects in Python](https://slightlysharpe.com/blog/automagically-increment-objects-in-python).

## Get it & run it 

Grab this code and make it your own. Tests w/full coverage are included. 

### Clone the repo: 

```
git clone git@github.com:thinkjrs/demo-code.git 
``` 

### Build your environment 
First, move into the correct directory: 

```bash 
cd automagically-increment-objects-in-python
```

Then setup your environment. 

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

This contains three main files: 

- `counter.py`: An initial outline of usage for the `collections.Counter` data structure.
- `inventory.py`: A module to house the `Inventory` class and other related items.
- `managedb.py`: A simple local data store and retrieval for the `Inventory` class.

It of course includes unit tests: 
- `test_counter.py` 
- `test_inventory.py` 
- `test_managedb.py`

### Other goodies 

This contains a `pyproject.toml` with basic pytest defaults we use @ [Tincre](https://tincre.com). To run
tests and get a nice terminal coverage printout simply run `pytest` after you've activated your virtual environment, 
as above.

## Contributions 

If you find a mistake or means for improvement please open a PR or file an issue herein. 

A huge thanks and much ❤ in advance!
