# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("load_window", __name__)


@bp.route("/load_window", methods=["POST"])
def load_window():
    summary = request.get_data(as_text=True)
    reader = make_reader(summary)
    cohort = reader()
    return '<div>' + str(cohort) + '</div>'
