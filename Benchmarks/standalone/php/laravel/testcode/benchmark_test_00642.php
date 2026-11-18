<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class BenchmarkTest00642Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $_valid = Validator::make(['value' => (string)$data], ['value' => ['regex:' . '#^[a-zA-Z0-9 _.%\\-]+$#']]);
        if ($_valid->fails()) { error_log('schema validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = (string)$data;
        system('gzip -f /var/app/reports/' . (string)$processed);
        return response()->json(['ok' => 1]);
    }
}
