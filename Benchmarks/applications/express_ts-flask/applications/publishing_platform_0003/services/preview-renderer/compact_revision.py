# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("compact_revision", __name__)


@bp.route("/compact_revision/<path_param>", methods=["POST"])
def compact_revision(path_param):
    heading = path_param
    def normalize(value):
        return value.strip()
    addendum = normalize(heading)
    byline = bleach.clean(markdown.markdown(addendum))
    return '<div>' + str(byline) + '</div>'
