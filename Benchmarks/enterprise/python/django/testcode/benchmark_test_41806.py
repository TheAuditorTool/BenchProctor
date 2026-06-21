# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest41806(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
