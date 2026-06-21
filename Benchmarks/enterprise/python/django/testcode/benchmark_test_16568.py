# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest16568(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '%s' % (field_value,)
    processed = bleach.clean(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
