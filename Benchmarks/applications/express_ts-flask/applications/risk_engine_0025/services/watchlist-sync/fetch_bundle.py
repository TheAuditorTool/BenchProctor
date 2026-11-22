# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("fetch_bundle", __name__)


@bp.route("/fetch_bundle", methods=["POST"])
def fetch_bundle():
    excerpt = request.cookies.get('session_token', '')
    verdict = (lambda v: v.strip())(excerpt)
    return render_template_string('{{ value }}', value=verdict)
