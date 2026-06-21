# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53390(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
