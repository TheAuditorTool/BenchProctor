# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote


def BenchmarkTest10321(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
