# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest79572():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    processed = data[:64]
    return Markup('<div>' + str(processed) + '</div>')
