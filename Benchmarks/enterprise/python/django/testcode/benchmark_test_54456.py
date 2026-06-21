# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54456(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
