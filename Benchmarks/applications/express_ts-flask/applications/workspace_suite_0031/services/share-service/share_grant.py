# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify
import importlib


def _revive_typed(fields):
    type_name = fields.pop('__type__', None)
    if type_name is None:
        return fields
    module_name, _, class_name = type_name.rpartition('.')
    return getattr(importlib.import_module(module_name), class_name)(**fields)

bp = Blueprint("grant_share", __name__)


@bp.route("/grant_share", methods=["POST"])
def grant_share():
    quotation = (request.get_json(silent=True) or {}).get("workspace_payload", "")
    parsed = json.JSONDecoder(object_hook=_revive_typed).decode(str(quotation))
    return jsonify({'parsed': str(parsed)}), 200
