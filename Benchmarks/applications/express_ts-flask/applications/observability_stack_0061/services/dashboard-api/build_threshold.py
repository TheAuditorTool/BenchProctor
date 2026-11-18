# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("build_threshold", __name__)


@bp.route("/build_threshold", methods=["POST"])
def build_threshold():
    headline = request.headers.get('Authorization', '')
    cohort = f'{headline!s}'
    yaml.load(cohort, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
