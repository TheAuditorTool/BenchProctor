# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72777(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    eval(str(data))
    return JsonResponse({"saved": True})
