import pytest
from flaskblog import create_app

@pytest.fixture
def client():
  app = create_app()

  with app.app_context():
    yield app.test_client()
    app.testing = True
    client = app.test_client()





# import os
# import tempfile
# @pytest.fixture
# def client():
#     db_fd, os.environ.get['SQLALCHEMY_DATABASE_URI'] = tempfile.mkstemp()
#     app = create_app()

#     with app.app_context():
#       yield app.test_client()

#     os.close(db_fd)
#     os.unlink(os.environ.get['SQLALCHEMY_DATABASE_URI'])

#     app.testing = True
#     client = app.test_client()