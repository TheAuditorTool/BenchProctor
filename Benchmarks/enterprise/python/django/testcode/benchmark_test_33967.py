# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote


def BenchmarkTest33967(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
