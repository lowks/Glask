from flask import url_for
from glask import current_for, Glask

app = Glask(__name__)


@app.route('/glask')
def show_glask():
    return 'hello glask'


def test_current_for():
    with app.test_request_context('/glask'):
        assert current_for() == url_for('show_glask')

    # test can access current_for in jinja
    assert app.jinja_env.globals.get('current_for') == current_for
