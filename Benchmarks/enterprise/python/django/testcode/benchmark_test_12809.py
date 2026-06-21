# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest12809(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
