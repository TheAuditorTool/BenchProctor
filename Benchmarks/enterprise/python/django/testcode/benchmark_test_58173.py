# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest58173(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
