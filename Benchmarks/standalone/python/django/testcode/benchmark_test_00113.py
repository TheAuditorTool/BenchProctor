# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00113(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
