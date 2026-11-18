<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00053Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        if (!preg_match('#^[a-zA-Z0-9 _.\\-]+$#', $data)) { error_log('input validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        session(['data' => (string) $processed]);
        return response()->json(['ok' => 1]);
    }
}
