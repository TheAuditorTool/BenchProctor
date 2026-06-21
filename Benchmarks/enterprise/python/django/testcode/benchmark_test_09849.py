# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09849(request):
    raw_body = request.body.decode('utf-8')
    data = '{}'.format(raw_body)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
