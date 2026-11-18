# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("reconcile_record", __name__)


@bp.route("/reconcile_record/<path_param>", methods=["POST"])
def reconcile_record(path_param):
    transcript = path_param
    backorder, _sep, _rest = str(transcript).partition('\x00')
    restock = bleach.clean(markdown.markdown(backorder))
    return '<div>' + str(restock) + '</div>'
