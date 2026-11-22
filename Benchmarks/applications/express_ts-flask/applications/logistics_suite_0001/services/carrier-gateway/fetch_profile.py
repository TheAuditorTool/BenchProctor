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

bp = Blueprint("fetch_profile", __name__)


@bp.route("/fetch_profile", methods=["POST"])
def fetch_profile():
    quotation = request.headers.get('X-Forwarded-For', '')
    def normalize(value):
        return value.strip()
    parcel = normalize(quotation)
    parsed = json.JSONDecoder(object_hook=_revive_typed).decode(str(parcel))
    return jsonify({'parsed': str(parsed)}), 200
