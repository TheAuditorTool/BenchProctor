# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest28541(request):
    raw_body = request.body.decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
