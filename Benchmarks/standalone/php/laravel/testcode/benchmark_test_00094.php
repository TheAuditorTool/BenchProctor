<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00094Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        $_coerced = (float)$data;
        $processed = $_coerced;
        \Illuminate\Support\Facades\Session::put(['data' => (string) $processed, 'data_updated_at' => time()]);
        return response()->json(['ok' => 1]);
    }
}
