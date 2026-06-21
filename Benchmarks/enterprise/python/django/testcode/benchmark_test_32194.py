# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import db, User


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest32194(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = field_value if field_value else 'default'
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
