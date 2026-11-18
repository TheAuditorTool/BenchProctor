<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00716Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT body FROM mq_messages ORDER BY id DESC LIMIT 1')->body;
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
