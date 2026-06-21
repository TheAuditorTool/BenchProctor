# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote


def BenchmarkTest09599(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return JsonResponse({"saved": True})
