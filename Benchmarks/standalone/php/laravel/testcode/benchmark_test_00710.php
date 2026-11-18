<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00710Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $data = vsprintf('%1$s', [$userInput]);
        $result = DB::table('users')->where('id', $data)->first();
        $value = $result->name;
        return response()->json(['ok' => 1]);
    }
}
