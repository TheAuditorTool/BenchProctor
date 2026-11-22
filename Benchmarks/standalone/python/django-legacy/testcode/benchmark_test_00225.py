# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00225(request):
    multipart_value = request.POST.get('multipart_field', '')
    pending = list(str(multipart_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    if label is None:
        return JsonResponse({'error': 'unknown plan'}, status=404)
    value = label.upper()
    return JsonResponse({'plan': value}, status=200)
