# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest35325(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
