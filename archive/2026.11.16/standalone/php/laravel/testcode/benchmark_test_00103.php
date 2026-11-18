<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00103Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        $_prefix = strtolower(substr($userInput, 0, 1));
        $data = '';
        switch ($_prefix) {
            case 'h': $data = strtolower($userInput); break;
            case 'f': $data = strtoupper($userInput); break;
            default: $data = trim($userInput); break;
        }
        $ciphertext = openssl_encrypt((string)$data, 'des-ecb', getenv('DATA_ENC_KEY'));
        return response()->json(['ok' => 1]);
    }
}
