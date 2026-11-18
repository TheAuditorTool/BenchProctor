<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00697Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        $ciphertext = openssl_encrypt((string)$data, 'des-ecb', getenv('DATA_ENC_KEY'));
        return response()->json(['ok' => 1]);
    }
}
