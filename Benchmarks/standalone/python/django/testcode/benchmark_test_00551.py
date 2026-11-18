# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect
from app_runtime import db


def BenchmarkTest00551(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = str(comment_value).replace('\x00', '')
    return redirect(str(data))
