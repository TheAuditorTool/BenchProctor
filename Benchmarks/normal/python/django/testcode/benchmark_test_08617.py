# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest08617(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
