# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
from urllib.parse import unquote


def BenchmarkTest06537(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
