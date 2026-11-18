<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class BenchmarkTest00295Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->route('id') ?? $request->input('id', ''));
        $data = vsprintf('%1$s', [$userInput]);
        $_valid = Validator::make(['value' => (string)$data], ['value' => ['regex:' . '#^[a-zA-Z0-9 _.%\\-]+$#']]);
        if ($_valid->fails()) { error_log('schema validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = (string)$data;
        shell_exec('bash -c "grep -r ' . $processed . ' /var/app/logs"');
        return response()->json(['ok' => 1]);
    }
}
