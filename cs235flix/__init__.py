"""Initialize Flask app."""

import os

from flask import Flask

import cs235flix.adapters.repository as repo
from cs235flix.adapters.memory_repository import MemoryRepository, populate


def create_app(test_config=None):

    app = Flask(__name__)

    app.config.from_object('config.Config')
    data_path = "cs235flix/adapters/data/Data1000Movies.csv"

    # If this is a test (called from test/conftest.client)
    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    # Create the MemoryRepository implementation for a memory-based repository.
    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)

    # Build the application - these steps require an application context.
    with app.app_context():
    #     Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .advsearch import advsearch
        app.register_blueprint(advsearch.advsearch_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

        from .watchlist import watchlist
        app.register_blueprint(watchlist.watchlist_blueprint)
    return app
