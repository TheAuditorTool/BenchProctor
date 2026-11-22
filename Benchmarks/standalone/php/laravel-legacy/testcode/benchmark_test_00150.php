<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00150Controller
{
    public function __invoke()
    {
        $userInput = \Illuminate\Support\Facades\Redis::get('user_data');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $identQuote = in_array(DB::getDriverName(), ['mysql', 'mariadb'], true) ? '`' : '"';
        DB::select('SELECT * FROM users WHERE ' . $identQuote . str_replace($identQuote, $identQuote . $identQuote, (string)$data) . $identQuote . ' = 1');
        return response()->json(['ok' => 1]);
    }
}
