# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("compact_cart", __name__)


@bp.route("/compact_cart/<path_param>", methods=["POST"])
def compact_cart(path_param):
    memo = path_param
    voucher, _sep, _rest = str(memo).partition('\x00')
    backorder = bleach.clean(markdown.markdown(voucher))
    return '<div>' + str(backorder) + '</div>'
