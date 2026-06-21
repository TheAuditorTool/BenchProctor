# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61834(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
