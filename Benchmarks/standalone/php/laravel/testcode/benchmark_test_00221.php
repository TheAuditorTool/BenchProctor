<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00221Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $rows = DB::table('users')->where('id', $data)->get();
        return response()->json(['ok' => 1]);
    }
}
