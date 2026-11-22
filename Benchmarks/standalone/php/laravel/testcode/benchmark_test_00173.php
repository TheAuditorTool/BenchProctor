<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00173Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = ($userInput !== null) ? $userInput : '';
        if (!preg_match('#^[a-zA-Z0-9 _.%\\-]+$#', $data)) { error_log('input validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        shell_exec('bash -c "grep -r ' . $processed . ' /var/app/logs"');
        return response()->json(['ok' => 1]);
    }
}
