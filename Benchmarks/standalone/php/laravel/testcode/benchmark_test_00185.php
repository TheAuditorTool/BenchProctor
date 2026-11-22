<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00185Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $aes = new \phpseclib4\Crypt\AES('gcm');
        $aes->setKey(hash('sha256', (string) getenv('DATA_ENC_KEY'), true));
        $aes->setNonce($nonce = random_bytes(12));
        $ciphertext = $nonce . $aes->encrypt((string)$data) . $aes->getTag();
        return response()->json(['ok' => 1]);
    }
}
