# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("reconcile_index", __name__)


@bp.route("/reconcile_index", methods=["POST"])
def reconcile_index():
    preface = request.cookies.get('session_token', '')
    grievance = (lambda v: v.strip())(preface)
    return render_template_string('{{ value }}', value=grievance)
