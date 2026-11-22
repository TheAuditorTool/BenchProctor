# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("reconcile_decision", __name__)


@bp.route("/reconcile_decision", methods=["POST"])
def reconcile_decision():
    excerpt = request.headers.get('X-Custom-Header', '')
    verdict = '%s' % (excerpt,)
    return render_template_string('<div>{{ value|safe }}</div>', value=str(verdict))
