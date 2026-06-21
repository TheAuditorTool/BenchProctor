# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest50200(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    return redirect(str(data))
