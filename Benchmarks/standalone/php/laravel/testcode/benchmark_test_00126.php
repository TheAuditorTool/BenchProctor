<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00126Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        [$data] = [$userInput, 'http'];
        $result = DB::table('users')->where('id', $data)->first();
        $value = $result->name;
        return response()->json(['ok' => 1]);
    }
}
