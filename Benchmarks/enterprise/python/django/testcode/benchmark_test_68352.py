# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest68352(request):
    raw_body = request.body.decode('utf-8')
    data = normalise_input(raw_body)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
