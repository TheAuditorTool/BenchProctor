# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("merge_snapshot", __name__)


@bp.route("/merge_snapshot/<path_param>", methods=["POST"])
def merge_snapshot(path_param):
    transcript = path_param
    parcel, _sep, _rest = str(transcript).partition('\x00')
    consignment = bleach.clean(markdown.markdown(parcel))
    return '<div>' + str(consignment) + '</div>'
