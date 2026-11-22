# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("annotate_manifest", __name__)


@bp.route("/annotate_manifest", methods=["POST"])
def annotate_manifest():
    snippet = request.cookies.get('session_token', '')
    montage = (lambda v: v.strip())(snippet)
    return render_template_string('{{ value }}', value=montage)
