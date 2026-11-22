<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00348Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT name FROM users LIMIT 1')->name;
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $salt = random_bytes(16);
        $rc4 = new \phpseclib4\Crypt\RC4();
        $rc4->setKey(hash_hmac('sha256', $salt, (string) getenv('DATA_ENC_KEY'), true));
        $ciphertext = $salt . $rc4->encrypt((string)$data);
        return response()->json(['ok' => 1]);
    }
}
