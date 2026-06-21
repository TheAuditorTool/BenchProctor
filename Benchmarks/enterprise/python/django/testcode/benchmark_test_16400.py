# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16400(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % (raw_body,)
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
