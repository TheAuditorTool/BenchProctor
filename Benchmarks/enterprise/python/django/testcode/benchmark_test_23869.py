# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23869(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % (raw_body,)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
