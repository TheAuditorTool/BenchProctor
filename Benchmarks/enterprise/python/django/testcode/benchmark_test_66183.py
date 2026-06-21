# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest66183(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ctx = RequestContext(field_value)
    data = ctx.payload
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
