# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00125(request):
    raw_body = request.body.decode('utf-8')
    kind = 'json' if str(raw_body).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(raw_body).strip()
        case _:
            data = str(raw_body)
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    value = label.upper()
    return JsonResponse({'plan': value}, status=200)
