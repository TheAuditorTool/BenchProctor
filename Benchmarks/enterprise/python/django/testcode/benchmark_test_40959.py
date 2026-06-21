# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def ensure_str(value):
    return str(value)

def BenchmarkTest40959(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ensure_str(auth_header)
    processed = data[:64]
    return redirect(str(processed))
