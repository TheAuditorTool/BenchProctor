<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00185Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        $salt = random_bytes(16);
        $rc4 = new \phpseclib3\Crypt\RC4();
        $rc4->setKey(hash_hmac('sha256', $salt, (string) getenv('DATA_ENC_KEY'), true));
        $ciphertext = $salt . $rc4->encrypt((string)$data);
        return response()->json(['ok' => 1]);
    }
}
