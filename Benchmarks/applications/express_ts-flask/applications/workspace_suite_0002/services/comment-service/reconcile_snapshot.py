# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("reconcile_snapshot", __name__)


@bp.route("/reconcile_snapshot/<path_param>", methods=["POST"])
def reconcile_snapshot(path_param):
    transcript = path_param
    heading, _sep, _rest = str(transcript).partition('\x00')
    passage = bleach.clean(markdown.markdown(heading))
    return '<div>' + str(passage) + '</div>'
