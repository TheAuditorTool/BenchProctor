# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00069(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    value = label.upper()
    return JsonResponse({'plan': value}, status=200)
