# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import urlparse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest43428(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return redirect(str(target_url))
