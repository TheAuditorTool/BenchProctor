# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import db


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest27628(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '%s' % (field_value,)
    if data != request.session.get('csrf_token'):
        return JsonResponse({'error': 'CSRF token mismatch'}, status=403)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return JsonResponse({"saved": True})
