# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import asyncio
from app_runtime import db, User


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest10379(request):
    field_value = UserForm(request.POST).data.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
