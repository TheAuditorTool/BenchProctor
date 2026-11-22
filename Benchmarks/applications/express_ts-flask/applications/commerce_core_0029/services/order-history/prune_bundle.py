# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("prune_bundle", __name__)


@bp.route("/prune_bundle", methods=["POST"])
def prune_bundle():
    notice = request.cookies.get('session_token', '')
    backorder = (lambda v: v.strip())(notice)
    return render_template_string('{{ value }}', value=backorder)
