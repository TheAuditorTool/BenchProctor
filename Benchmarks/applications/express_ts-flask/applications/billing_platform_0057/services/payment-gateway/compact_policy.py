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

bp = Blueprint("compact_policy", __name__)


@bp.route("/compact_policy", methods=["POST"])
def compact_policy():
    caption = request.headers.get('X-Forwarded-For', '')
    def normalize(value):
        return value.strip()
    remittance = normalize(caption)
    parsed = json.JSONDecoder(object_hook=_revive_typed).decode(str(remittance))
    return jsonify({'parsed': str(parsed)}), 200
