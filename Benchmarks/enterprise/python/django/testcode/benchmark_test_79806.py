# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def BenchmarkTest79806(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    return redirect(str(data))
