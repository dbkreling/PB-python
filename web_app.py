from flask import Flask, jsonify, render_template, request, redirect
from tests import *
from flask_sqlalchemy import SQLAlchemy
import unittest
import importlib
from datetime import datetime
import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'profitbricks.sqlite')
db = SQLAlchemy(app)
files = [f[:-3] for f in os.listdir("./tests") if not f.startswith("__init__") and f.endswith(".py")]

class Tests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requester = db.Column(db.String(80), nullable=False)
    path_to_test = db.Column(db.String(80))
    test_cases = db.Column(db.Integer)
    time_stamp = db.Column(db.DateTime())
    failures = db.Column(db.String)
    was_successful = db.Column(db.Boolean())


@app.route("/test/list", methods=["GET"])
def show_results():
    """ Display results of the tests"""
    cursor = db.engine.execute('SELECT requester, path_to_test, test_cases, \
                        time_stamp, failures, was_successful FROM tests')
    items = [dict(requester=row[0], path_to_test=row[1], test_cases=row[2],
                  time_stamp=row[3], failures=[4], was_successful=row[5])
             for row in cursor.fetchall()]
    return jsonify(items)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/test/submit", methods=["GET", "POST"])
def run_tests():
    if request.method == "GET":
        return render_template("submit_test.html", option_list=files)
    else:
        # Collect data from submit_test.html
        requester = request.form["requester"]
        path_to_test = request.form["path_to_test"]
        test_name = request.form["test_name"]

        # User specified a path to a test file
        if path_to_test:
            basename = os.path.basename(path_to_test)
            if basename.endswith(".py"):
                test_name = basename[:-3]
            else:
                raise ImportError(message="Wrong test file or file path")
        else:
            path_to_test = basedir + "/tests/" + test_name

        # Change test_name to be imported in the correct format
        test_name = "tests." + test_name
        test_module = importlib.import_module(test_name)


        test = trigger_unittest(requester, path_to_test, test_module)

        save_to_db(test)

        return redirect("/test/list")


def trigger_unittest(requester, path_to_test, test_module):
    """ Load and run test selected on the web UI """
    test_loader = test_module.unittest.TestLoader()
    # tests = test_loader.discover(testdir_path)
    selected_test = test_loader.loadTestsFromModule(test_module)
    test_result = unittest.TestResult()
    selected_test.run(test_result)

    failures = "None" if test_result.wasSuccessful() else test_result.failures[0][1]
    was_successful = test_result.wasSuccessful()
    time_stamp = datetime.now()

    test = Tests(requester=requester, path_to_test=path_to_test,
                 test_cases=selected_test.countTestCases(),
                 time_stamp=time_stamp, failures=failures,
                 was_successful=was_successful)

    return test


def save_to_db(test):
    """ Save test data to database table"""
    db.session.add(test)
    db.session.commit()


if __name__ == "__main__":
    app.run()
