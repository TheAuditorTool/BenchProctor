# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00192(request):
    field_value = request.POST.get('field', '')
    data = '%s' % str(field_value)
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    if label is None:
        return JsonResponse({'error': 'unknown plan'}, status=404)
    value = label.upper()
    return JsonResponse({'plan': value}, status=200)
