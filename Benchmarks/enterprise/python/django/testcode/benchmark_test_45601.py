# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest45601(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '%s' % (field_value,)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
