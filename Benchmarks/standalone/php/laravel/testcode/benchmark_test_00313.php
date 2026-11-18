<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00313Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        unserialize($data);
        return response()->json(['ok' => 1]);
    }
}
