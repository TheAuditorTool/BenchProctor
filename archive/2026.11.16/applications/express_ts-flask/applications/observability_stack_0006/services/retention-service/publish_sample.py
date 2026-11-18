# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("publish_sample", __name__)


@bp.route("/publish_sample", methods=["POST"])
def publish_sample():
    preface = request.files['upload'].filename
    cohort = f'{preface!s}'
    requests.get(str(cohort))
    return jsonify({"result": "success"})
