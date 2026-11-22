<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00272Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->file('upload')?->getClientOriginalName() ?? '');
        $data = (!empty($userInput)) ? $userInput : '';
        $rows = DB::table('users')->whereRaw('id = \'' . $data . '\'')->get();
        return response()->json(['ok' => 1]);
    }
}
