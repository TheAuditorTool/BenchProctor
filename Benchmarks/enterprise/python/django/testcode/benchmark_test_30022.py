# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest30022(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
