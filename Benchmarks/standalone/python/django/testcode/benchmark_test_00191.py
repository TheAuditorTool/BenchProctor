# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00191(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    exec(str(processed))
    return JsonResponse({"saved": True})
