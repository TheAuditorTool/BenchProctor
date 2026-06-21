# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote


def BenchmarkTest73117(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
