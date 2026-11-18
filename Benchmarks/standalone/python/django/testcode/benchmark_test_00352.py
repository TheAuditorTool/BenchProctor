# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00352(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    form = FormData(payload=auth_header)
    data = form.payload
    return redirect(str(data))
