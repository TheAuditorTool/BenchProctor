# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("normalize_dispute", __name__)


@bp.route("/normalize_dispute", methods=["POST"])
def normalize_dispute():
    headline = request.headers.get('Referer', '')
    reader = make_reader(headline)
    disbursement = reader()
    remittance = bleach.clean(markdown.markdown(disbursement))
    return '<div>' + str(remittance) + '</div>'
