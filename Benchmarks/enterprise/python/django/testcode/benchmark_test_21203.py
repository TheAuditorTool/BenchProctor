# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse
from app_runtime import db


def BenchmarkTest21203(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ','.join(parts)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
