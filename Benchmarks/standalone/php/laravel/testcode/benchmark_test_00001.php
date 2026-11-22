<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00001Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT body FROM mq_messages ORDER BY id DESC LIMIT 1')->body;
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        file_get_contents((string)$data);
        return response()->json(['ok' => 1]);
    }
}
