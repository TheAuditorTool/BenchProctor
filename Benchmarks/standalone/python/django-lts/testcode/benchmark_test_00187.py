# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00187(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % (auth_header,)
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    if label is None:
        return JsonResponse({'error': 'unknown plan'}, status=404)
    value = label.upper()
    return JsonResponse({'plan': value}, status=200)
