<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00224Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT body FROM mq_messages ORDER BY id DESC LIMIT 1')->body;
        $data = sprintf('%s', $userInput);
        \App\Models\User::where('id', $data)->get();
        return response()->json(['ok' => 1]);
    }
}
