# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35352(request):
    upload_name = request.FILES['upload'].name
    data, _sep, _rest = str(upload_name).partition('\x00')
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
