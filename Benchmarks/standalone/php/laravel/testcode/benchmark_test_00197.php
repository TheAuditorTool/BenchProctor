<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00197Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $result = DB::table('users')->where('id', $data)->first();
        $value = $result->name;
        return response()->json(['ok' => 1]);
    }
}
