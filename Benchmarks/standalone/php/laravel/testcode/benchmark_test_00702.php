<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00702Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $data = hex2bin($userInput);
        if (!preg_match('#^(asc|desc|name|created)$#', (string)$data)) { error_log('enum validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        DB::select('SELECT * FROM users ORDER BY ' . $processed);
        return response()->json(['ok' => 1]);
    }
}
