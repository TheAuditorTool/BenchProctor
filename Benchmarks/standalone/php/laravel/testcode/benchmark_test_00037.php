<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00037Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        return response()->json(['ok' => 1])->cookie('session', (string)$data, 0, '/', null, false, true, false, 'Strict');
    }
}
