<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00409Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $result = DB::table('users')->where('id', $data)->first();
        if ($result === null) { return response()->json(["error" => "not found"], 404); }
        $value = $result->name;
        return response()->json(['ok' => 1]);
    }
}
