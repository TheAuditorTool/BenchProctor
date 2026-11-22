# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("merge_profile", __name__)


@bp.route("/merge_profile/<path_param>", methods=["POST"])
def merge_profile(path_param):
    notice = path_param
    def normalize(value):
        return value.strip()
    backorder = normalize(notice)
    voucher = bleach.clean(markdown.markdown(backorder))
    return '<div>' + str(voucher) + '</div>'
