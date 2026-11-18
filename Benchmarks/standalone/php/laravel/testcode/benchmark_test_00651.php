<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00651Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = sprintf('%s', $userInput);
        if (!preg_match('#^[a-zA-Z0-9_.\\#\\-]+$#', $data)) { error_log('input validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        DB::select('SELECT * FROM users WHERE id = \'' . $processed . '\'');
        return response()->json(['ok' => 1]);
    }
}
