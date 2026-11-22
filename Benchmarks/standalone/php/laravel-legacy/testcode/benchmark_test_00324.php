<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00324Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        $sealed = base64_decode((string)$data, true) ?: '';
        $claims = openssl_decrypt(substr($sealed, 28), 'aes-256-gcm', getenv('DATA_ENC_KEY'), OPENSSL_RAW_DATA, substr($sealed, 0, 12), substr($sealed, 12, 16));
        return response()->json(['ok' => 1]);
    }
}
