# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00034(request):
    env_value = os.environ.get('APP_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    if label is None:
        return JsonResponse({'error': 'unknown plan'}, status=404)
    value = label.upper()
    return JsonResponse({'plan': value}, status=200)
