# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest22577(request):
    user_id = request.GET.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
