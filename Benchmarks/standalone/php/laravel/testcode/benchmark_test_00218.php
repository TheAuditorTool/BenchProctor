<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00218Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('User-Agent', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $result = DB::table('users')->where('id', $data)->first();
        $value = $result->name;
        return response()->json(['ok' => 1]);
    }
}
