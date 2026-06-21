# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest72715(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body}'
    return redirect(str(data))
