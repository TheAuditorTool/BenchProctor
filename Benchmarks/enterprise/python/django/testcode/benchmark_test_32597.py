# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32597(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    int(str(data))
    return JsonResponse({"saved": True})
