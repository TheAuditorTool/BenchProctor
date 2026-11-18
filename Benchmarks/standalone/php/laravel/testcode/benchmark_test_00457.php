<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class BenchmarkTest00457Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $_valid = Validator::make(['value' => (string)$data], ['value' => ['regex:' . '#^[a-zA-Z0-9 _.\\-]+$#']]);
        if ($_valid->fails()) { error_log('schema validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = (string)$data;
        session(['data' => (string) $processed]);
        return response()->json(['ok' => 1]);
    }
}
