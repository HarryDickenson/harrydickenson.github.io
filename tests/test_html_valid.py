import os
from html5validator import Validator

def test_index_html_valid():
    html_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'index.html'))
    v = Validator()
    errors = v.validate([html_file])
    assert errors == 0, f"HTML validation failed with {errors} errors"
