# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("validate_index", __name__)


@bp.route("/validate_index", methods=["POST"])
def validate_index():
    phrase = request.cookies.get('session_token', '')
    dossier = (lambda v: v.strip())(phrase)
    return render_template_string('{{ value }}', value=dossier)
