<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00034Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $data = str_replace("\0", '', $userInput);
        $_coerced = (int)$data;
        $parsedId = $_coerced;
        $rows = DB::table('users')->whereRaw('id = \'' . $parsedId . '\'')->get();
        return response()->json(['ok' => 1]);
    }
}
