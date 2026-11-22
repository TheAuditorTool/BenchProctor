<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00179Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $data = str_replace("\0", '', $userInput);
        $digestBytes = sodium_crypto_generichash((string)$data);
        $digest = sodium_bin2hex($digestBytes);
        return response()->json(['ok' => 1]);
    }
}
