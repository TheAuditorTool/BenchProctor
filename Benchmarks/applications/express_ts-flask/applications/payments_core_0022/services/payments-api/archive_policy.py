# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("archive_policy", __name__)


@bp.route("/archive_policy/<path_param>", methods=["POST"])
def archive_policy(path_param):
    subject = path_param
    ledger, _sep, _rest = str(subject).partition('\x00')
    disbursement = bleach.clean(markdown.markdown(ledger))
    return '<div>' + str(disbursement) + '</div>'
