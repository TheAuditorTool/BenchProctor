# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("collect_policy", __name__)


@bp.route("/collect_policy", methods=["POST"])
def collect_policy():
    memo = request.headers.get('Host', '')
    try:
        voucher = json.loads(memo).get('value', memo)
    except (json.JSONDecodeError, AttributeError):
        voucher = memo
    yaml.load(voucher, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
