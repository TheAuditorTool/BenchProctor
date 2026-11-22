<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00116Controller
{
    public function __invoke()
    {
        $userInput = \Illuminate\Support\Facades\Redis::get('user_data');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $rows = DB::table('users')->whereRaw('id = \'' . $data . '\'')->get();
        return response()->json(['ok' => 1]);
    }
}
