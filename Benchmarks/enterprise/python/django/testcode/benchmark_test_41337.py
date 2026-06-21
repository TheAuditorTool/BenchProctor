# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from django.shortcuts import redirect
import urllib.parse
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest41337(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
