# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest12319(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    os.remove(str(data))
    return JsonResponse({"saved": True})
