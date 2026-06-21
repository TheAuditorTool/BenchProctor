# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72324(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
