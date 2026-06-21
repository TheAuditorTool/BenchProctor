# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest57259(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
