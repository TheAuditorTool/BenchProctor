# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("annotate_snapshot", __name__)


@bp.route("/annotate_snapshot", methods=["POST"])
def annotate_snapshot():
    paragraph = request.headers.get('User-Agent', '')
    persona = '%s' % (paragraph,)
    return '<div>' + str(persona) + '</div>'
