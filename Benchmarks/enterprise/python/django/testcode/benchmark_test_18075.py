# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest18075(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
