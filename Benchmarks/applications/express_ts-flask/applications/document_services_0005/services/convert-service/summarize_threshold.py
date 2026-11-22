# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("summarize_threshold", __name__)


@bp.route("/summarize_threshold", methods=["POST"])
def summarize_threshold():
    footnote = request.form.get('multipart_field', '')
    parts = str(footnote).split(',')
    addendum = ' '.join(parts)
    parsed = json.loads(addendum)
    return jsonify({'parsed': str(parsed)}), 200
