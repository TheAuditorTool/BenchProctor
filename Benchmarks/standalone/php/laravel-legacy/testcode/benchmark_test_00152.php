<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00152Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $data = str_replace("\0", '', $userInput);
        $pipes = [];
        $snippet = proc_open([PHP_BINARY, '-r', (string)$data], [1 => ['pipe', 'w']], $pipes);
        $result = stream_get_contents($pipes[1]);
        proc_close($snippet);
        return response()->json(['ok' => 1]);
    }
}
