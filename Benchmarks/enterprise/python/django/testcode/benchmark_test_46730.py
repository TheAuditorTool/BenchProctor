# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest46730(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % (comment_value,)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
