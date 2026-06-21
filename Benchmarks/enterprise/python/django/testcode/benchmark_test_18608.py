# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18608(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
