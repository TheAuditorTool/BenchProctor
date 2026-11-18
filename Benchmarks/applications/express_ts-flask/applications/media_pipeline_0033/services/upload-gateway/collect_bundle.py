# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("collect_bundle", __name__)


@bp.route("/collect_bundle/<path_param>", methods=["POST"])
def collect_bundle(path_param):
    transcript = path_param
    rendition, _sep, _rest = str(transcript).partition('\x00')
    montage = bleach.clean(markdown.markdown(rendition))
    return '<div>' + str(montage) + '</div>'
