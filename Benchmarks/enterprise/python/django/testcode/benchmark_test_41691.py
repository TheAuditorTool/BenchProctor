# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest41691(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
