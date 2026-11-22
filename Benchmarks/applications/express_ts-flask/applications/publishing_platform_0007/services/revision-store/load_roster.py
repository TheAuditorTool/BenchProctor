# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("load_roster", __name__)


@bp.route("/load_roster", methods=["POST"])
def load_roster():
    remark = request.form.get('field', '')
    byline, _sep, _rest = str(remark).partition('\x00')
    yaml.load(byline, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
