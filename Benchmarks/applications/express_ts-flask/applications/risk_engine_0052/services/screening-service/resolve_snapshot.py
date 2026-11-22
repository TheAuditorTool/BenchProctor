# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("resolve_snapshot", __name__)


@bp.route("/resolve_snapshot", methods=["POST"])
def resolve_snapshot():
    memo = request.cookies.get('session_token', '')
    verdict = (lambda v: v.strip())(memo)
    return render_template_string('{{ value }}', value=verdict)
