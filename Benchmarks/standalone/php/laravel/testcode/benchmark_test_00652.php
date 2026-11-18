<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00652Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $data = ($userInput !== null) ? $userInput : '';
        $result = DB::table('users')->where('id', $data)->first();
        if ($result === null) { return response()->json(["error" => "not found"], 404); }
        $value = $result->name;
        return response()->json(['ok' => 1]);
    }
}
