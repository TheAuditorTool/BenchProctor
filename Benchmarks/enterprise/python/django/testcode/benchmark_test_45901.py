# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45901(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
