<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00167Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('X-Custom-Header', '');
        $result = DB::table('users')->where('id', $userInput)->first();
        $value = $result->name;
        return response()->json(['ok' => 1]);
    }
}
