# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote


def BenchmarkTest02038(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
