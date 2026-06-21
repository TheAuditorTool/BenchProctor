# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20825(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % str(upload_name)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
