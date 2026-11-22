# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import json
from flask import Blueprint, request, jsonify
import importlib


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'
def _revive_typed(fields):
    type_name = fields.pop('__type__', None)
    if type_name is None:
        return fields
    module_name, _, class_name = type_name.rpartition('.')
    return getattr(importlib.import_module(module_name), class_name)(**fields)

bp = Blueprint("audit_bundle", __name__)


@bp.route("/audit_bundle", methods=["POST"])
def audit_bundle():
    paragraph = request.form.get('multipart_field', '')
    form = FormData(payload=paragraph)
    gauge = form.payload
    parsed = json.JSONDecoder(object_hook=_revive_typed).decode(str(gauge))
    return jsonify({'parsed': str(parsed)}), 200
