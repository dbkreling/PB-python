from flask import Flask, jsonify, render_template, request, redirect
from tests import *
from flask_sqlalchemy import SQLAlchemy
import unittest
import importlib
import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'profitbricks.sqlite')
db = SQLAlchemy(app)
files = [f[:-3] for f in os.listdir("./tests") if not f.startswith("__init__") and f.endswith(".py")]

class Tests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requester = db.Column(db.String(80))
    path_to_test = db.Column(db.String(80))
    test_cases = db.Column(db.Integer)
    time_stamp = db.Column(db.DateTime())
    failures = db.Column(db.String)
    was_successful = db.Column(db.Boolean())


@app.route("/test/list", methods=["GET"])
def web_app(all_output=None):
    # print "web_app_print"
    return render_template("test_list.html")
    return jsonify(all_output)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/test/submit", methods=["GET", "POST"])
def run_tests():
    if request.method == "GET":
        return render_template("submit_test.html", option_list=files)
    else:
        requester = request.form["requester"]
        path_to_test = request.form["path_to_test"]
        test_name = request.form["test_name"]
        if path_to_test:
            test_name = path_to_test # todo fix this mess
        test_name = "tests." + test_name
        test_module = importlib.import_module(test_name)

        test = trigger_unittest(requester, path_to_test, test_module)


        # all_output = []
        # test_id = 0
        # f = {}
        # f["failures"] = "None" if test_result.wasSuccessful() else test_result.failures[0][1]
        # f["was_successful"] = test_result.wasSuccessful()
        # f["test_cases: "] = selected_test.countTestCases()  # todo insert Column
        # test_id = test_id + 1
        # f["id"] = test_id
        # all_output.append(f)
        # web_app(all_output)


        db.session.add(test)
        db.session.commit()

        return redirect("/test/list")

def trigger_unittest(requester, path_to_test, test_module):
    """ Load and run test selected on the web UI """
    test_loader = test_module.unittest.TestLoader()
    # tests = test_loader.discover(testdir_path)
    selected_test = test_loader.loadTestsFromModule(test_module)
    test_result = unittest.TestResult()
    selected_test.run(test_result)
    failures = "None" if test_result.wasSuccessful() else test_result.failures[0][1]
    test = Tests(requester=requester, path_to_test=path_to_test,
                 test_cases=selected_test.countTestCases(),
                 failures=failures,
                 was_successful=test_result.wasSuccessful())
    return test


if __name__ == "__main__":
    app.run()
