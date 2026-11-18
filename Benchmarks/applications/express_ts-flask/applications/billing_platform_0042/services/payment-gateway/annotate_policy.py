# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("annotate_policy", __name__)


@bp.route("/annotate_policy/<path_param>", methods=["POST"])
def annotate_policy(path_param):
    remark = path_param
    remittance, _sep, _rest = str(remark).partition('\x00')
    dunning = bleach.clean(markdown.markdown(remittance))
    return '<div>' + str(dunning) + '</div>'
