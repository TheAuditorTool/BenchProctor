# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def format_comment(request):
    preface = request.body.decode('utf-8')
    remark = preface if preface else 'default'
    parsed = yaml.safe_load(remark)
    return JsonResponse({'parsed': str(parsed)}, status=200)
