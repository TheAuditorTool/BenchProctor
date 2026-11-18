# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("export_digest", __name__)


@bp.route("/export_digest/<path_param>", methods=["POST"])
def export_digest(path_param):
    citation = path_param
    backorder, _sep, _rest = str(citation).partition('\x00')
    restock = bleach.clean(markdown.markdown(backorder))
    return '<div>' + str(restock) + '</div>'
