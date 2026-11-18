# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("merge_snapshot", __name__)


@bp.route("/merge_snapshot/<path_param>", methods=["POST"])
def merge_snapshot(path_param):
    headline = path_param
    disbursement, _sep, _rest = str(headline).partition('\x00')
    remittance = bleach.clean(markdown.markdown(disbursement))
    return '<div>' + str(remittance) + '</div>'
