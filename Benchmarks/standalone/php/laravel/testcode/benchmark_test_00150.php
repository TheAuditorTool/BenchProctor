<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00150Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Referer', '');
        $data = urldecode($userInput);
        if (!preg_match('#^[a-zA-Z0-9_.\\#\\-]+$#', $data)) { error_log('input validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        $rows = DB::table('users')->whereRaw('id = \'' . $processed . '\'')->get();
        return response()->json(['ok' => 1]);
    }
}
