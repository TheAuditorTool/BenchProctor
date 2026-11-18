<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00614Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        if (!preg_match('#^(asc|desc|name|created)$#', (string)$data)) { error_log('enum validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        DB::select('SELECT * FROM users ORDER BY ' . $processed);
        return response()->json(['ok' => 1]);
    }
}
