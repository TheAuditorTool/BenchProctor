# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("render_schedule", __name__)


@bp.route("/render_schedule/<path_param>", methods=["POST"])
def render_schedule(path_param):
    passage = path_param
    montage, _sep, _rest = str(passage).partition('\x00')
    rendition = bleach.clean(markdown.markdown(montage))
    return '<div>' + str(rendition) + '</div>'
