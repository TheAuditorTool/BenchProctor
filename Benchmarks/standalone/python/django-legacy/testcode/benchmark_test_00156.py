# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
import defusedxml.ElementTree
import json


def BenchmarkTest00156(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    parts = []
    for token in str(json_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    for _event, element in defusedxml.ElementTree.iterparse(io.BytesIO(str(data).encode()), events=('end',)):
        element.clear()
    return JsonResponse({"saved": True})
