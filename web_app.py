from flask import Flask, jsonify
from tests import *
import unittest
import os


app = Flask(__name__)


@app.route("/")
def web_app(files=None, testdir_path="."):
    if not files:
        # files = [f[:-3] for f in os.listdir("./tests") if
        #          not f.startswith("__init__") and f.endswith(".py")]
        files = [test_pass_0, test_all_failing, test_fail_2, test_pass_2,
                 test_all_passing, test_fail_1, test_all_tests, test_fail_0,
                 test_pass_1]
    all_output = []
    for f in files:
        # load testest_loaderoader submodules
        test_loader = unittest.TestLoader()
        # tests = test_loader.discover(testdir_path)
        test_module = test_loader.loadTestsFromModule(f)
        test_result = unittest.TestResult()
        test_module.run(test_result)

        f = {}
        f["failures"] = "None" if test_result.wasSuccessful() else test_result.failures[0][1]
        f["was_successful"] = test_result.wasSuccessful()
        f["test_cases: "] = test_module.countTestCases()
        all_output.append(f)
    return jsonify(all_output)


if __name__ == "__main__":
    app.run()
