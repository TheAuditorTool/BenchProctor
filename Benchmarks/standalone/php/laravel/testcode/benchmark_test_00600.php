<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00600Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $_prefix = strtolower(substr($userInput, 0, 1));
        $data = '';
        switch ($_prefix) {
            case 'h': $data = strtolower($userInput); break;
            case 'f': $data = strtoupper($userInput); break;
            default: $data = trim($userInput); break;
        }
        $digest = md5((string)$data);
        return response()->json(['ok' => 1]);
    }
}
