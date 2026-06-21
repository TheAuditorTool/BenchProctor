# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import auth_check


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest36029(request):
    field_value = UserForm(request.POST).data.get('field', '')
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if not auth_check(request.session.get('user', ''), str(data)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
