<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00329Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = vsprintf('%1$s', [$userInput]);
        $salt = random_bytes(16);
        $rc4 = new \phpseclib4\Crypt\RC4();
        $rc4->setKey(hash_hmac('sha256', $salt, (string) getenv('DATA_ENC_KEY'), true));
        $ciphertext = $salt . $rc4->encrypt((string)$data);
        return response()->json(['ok' => 1]);
    }
}
