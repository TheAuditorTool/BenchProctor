<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class BenchmarkTest00196Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = "{$userInput}";
        $_valid = Validator::make(['value' => (string)$data], ['value' => ['regex:' . '#^[a-zA-Z0-9 _.\\-]+$#']]);
        if ($_valid->fails()) { error_log('schema validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = (string)$data;
        \Illuminate\Support\Facades\Cache::forever('tenant:display_name', (string) $processed);
        return response()->json(['ok' => 1]);
    }
}
