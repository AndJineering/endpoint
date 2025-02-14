# endpoint

A common method of organizing files on a computer is to store them in hierarchical directories. 
This program implements commands that allow a user to create, move, and delete directories.

 * Running the program

You can edit `input.txt` and provide the list of commands expected to run. You can also make a new file
and call it as well.

Then run `python main.py input.txt` (or whatever your `python` path is set to, e.g. `python3`)

 * Running Tests

The tests use `pytest`

To use a virtual environment for this, do the following:
`python -m venv venv`
`source venv/bin/activate` # Unix based OS
`venv\Scripts\activate` # Windows
`pip -r requirements.txt`

Now `pytest` is installed.

Run the tests with `pytest test_directories.py`

When you're done, deactivate the virtual environment with
`deactivate`


