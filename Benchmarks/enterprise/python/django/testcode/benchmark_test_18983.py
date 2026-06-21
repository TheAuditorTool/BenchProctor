# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest18983(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ctx = RequestContext(field_value)
    data = ctx.payload
    if request.session.get('user') is None:
        return JsonResponse({'error': 'no session'}, status=401)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
