# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71089(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
