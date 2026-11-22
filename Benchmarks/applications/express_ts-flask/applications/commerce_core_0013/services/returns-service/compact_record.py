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

bp = Blueprint("compact_record", __name__)


@bp.route("/compact_record", methods=["POST"])
def compact_record():
    wording = request.form.get('multipart_field', '')
    form = FormData(payload=wording)
    backorder = form.payload
    parsed = json.JSONDecoder(object_hook=_revive_typed).decode(str(backorder))
    return jsonify({'parsed': str(parsed)}), 200
