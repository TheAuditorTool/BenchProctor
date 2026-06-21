# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from app_runtime import db


def BenchmarkTest13373():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value:.200s}'
    return Markup('<div>' + str(data) + '</div>')
