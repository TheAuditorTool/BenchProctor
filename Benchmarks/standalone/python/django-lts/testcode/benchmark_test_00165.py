# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00165(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    value = label.upper()
    return JsonResponse({'plan': value}, status=200)
