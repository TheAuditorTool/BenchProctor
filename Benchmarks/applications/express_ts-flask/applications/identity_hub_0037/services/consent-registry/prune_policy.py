# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("prune_policy", __name__)


@bp.route("/prune_policy", methods=["POST"])
def prune_policy():
    remark = request.form.get('field', '')
    pending = list(str(remark).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    persona = ','.join(collected)
    Path('/var/app/data/' + str(persona)).write_text('data')
    return jsonify({"result": "success"})
