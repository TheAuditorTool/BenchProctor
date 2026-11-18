<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00616Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT bio FROM profiles LIMIT 1')->bio;
        [$data] = [$userInput, 'http'];
        \App\Models\User::where('id', $data)->get();
        return response()->json(['ok' => 1]);
    }
}
