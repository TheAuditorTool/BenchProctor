# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01149(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % str(upload_name)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
