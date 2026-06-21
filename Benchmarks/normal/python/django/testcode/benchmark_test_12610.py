# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest12610(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
