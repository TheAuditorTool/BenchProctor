# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote


def BenchmarkTest57021(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return JsonResponse({"saved": True})
