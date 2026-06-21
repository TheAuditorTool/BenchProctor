# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56579(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
