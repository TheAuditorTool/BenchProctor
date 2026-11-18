# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("rotate_snapshot", __name__)


@bp.route("/rotate_snapshot/<path_param>", methods=["POST"])
def rotate_snapshot(path_param):
    note = path_param
    inquiry, _sep, _rest = str(note).partition('\x00')
    grievance = bleach.clean(markdown.markdown(inquiry))
    return '<div>' + str(grievance) + '</div>'
