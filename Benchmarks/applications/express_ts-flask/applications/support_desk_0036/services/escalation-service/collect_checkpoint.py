# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("collect_checkpoint", __name__)


@bp.route("/collect_checkpoint", methods=["POST"])
def collect_checkpoint():
    preface = request.cookies.get('session_token', '')
    grievance = (lambda v: v.strip())(preface)
    return render_template_string('{{ value }}', value=grievance)
