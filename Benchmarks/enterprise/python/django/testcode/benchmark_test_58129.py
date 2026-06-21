# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58129(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
