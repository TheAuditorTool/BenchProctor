# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00133(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    if label is None:
        return JsonResponse({'error': 'unknown plan'}, status=404)
    value = label.upper()
    return JsonResponse({'plan': value}, status=200)
