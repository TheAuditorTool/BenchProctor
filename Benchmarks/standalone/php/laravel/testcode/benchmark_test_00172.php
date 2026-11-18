<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00172Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $data = sprintf('%s', $userInput);
        $requested = (int) $data;
        $wrapped = unpack('l', pack('l', $requested + 1))[1];
        return response()->json(['wrapped' => $wrapped], 200);
    }
}
