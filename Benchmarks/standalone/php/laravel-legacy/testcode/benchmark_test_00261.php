<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00261Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $rows = DB::table('users')->whereRaw('id = \'' . $data . '\'')->get();
        return response()->json(['ok' => 1]);
    }
}
