<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00067Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $aes = new \phpseclib3\Crypt\AES('gcm');
        $aes->setKey(hash('sha256', (string) getenv('DATA_ENC_KEY'), true));
        $aes->setNonce($nonce = random_bytes(12));
        $ciphertext = $nonce . $aes->encrypt((string)$data) . $aes->getTag();
        return response()->json(['ok' => 1]);
    }
}
