# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest43500(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    return redirect(str(data))
