# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest25242(request):
    user_id = request.GET.get('id', '')
    os.system('echo ' + str(user_id))
    return JsonResponse({"saved": True})
