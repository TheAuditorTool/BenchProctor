# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
import markdown
import bleach


bp = Blueprint("fetch_sample", __name__)


@bp.route("/fetch_sample/<path_param>", methods=["POST"])
def fetch_sample(path_param):
    tagline = path_param
    def normalize(value):
        return value.strip()
    gauge = normalize(tagline)
    cohort = bleach.clean(markdown.markdown(gauge))
    return '<div>' + str(cohort) + '</div>'
