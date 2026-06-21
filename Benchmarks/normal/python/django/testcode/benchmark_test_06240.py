# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06240(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
