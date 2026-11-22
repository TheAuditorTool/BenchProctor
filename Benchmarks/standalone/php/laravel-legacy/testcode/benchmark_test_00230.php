<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class BenchmarkTest00230Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->route('id') ?? $request->input('id', ''));
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $token = (string) (int) (lcg_value() * 1000000000000);
        DB::statement('UPDATE users SET reset_token = ? WHERE email = ?', [$token, (string)$data]);
        return response()->json(['reset' => 'sent'], 200);
    }
}
