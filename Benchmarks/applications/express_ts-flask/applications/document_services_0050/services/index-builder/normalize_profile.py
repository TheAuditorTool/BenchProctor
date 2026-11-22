# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("normalize_profile", __name__)


@bp.route("/normalize_profile/<path_param>", methods=["POST"])
def normalize_profile(path_param):
    citation = path_param
    def normalize(value):
        return value.strip()
    dossier = normalize(citation)
    addendum = bleach.clean(markdown.markdown(dossier))
    return '<div>' + str(addendum) + '</div>'
