<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00073Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        if (!preg_match('#^[a-zA-Z0-9 _.%\\-]+$#', $data)) { error_log('input validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        system('gzip -f /var/app/reports/' . (string)$processed);
        return response()->json(['ok' => 1]);
    }
}
