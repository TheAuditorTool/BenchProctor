# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from app_runtime import db


def BenchmarkTest67326(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    return redirect(str(db_value))
