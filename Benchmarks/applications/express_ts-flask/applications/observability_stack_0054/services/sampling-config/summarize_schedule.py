# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("summarize_schedule", __name__)


@bp.route("/summarize_schedule/<path_param>", methods=["POST"])
def summarize_schedule(path_param):
    excerpt = path_param
    reader = make_reader(excerpt)
    cohort = reader()
    requests.get(str(cohort))
    return jsonify({"result": "success"})
