<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00354Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('variables.input', '');
        $_prefix = strtolower(substr($userInput, 0, 1));
        $data = '';
        switch ($_prefix) {
            case 'h': $data = strtolower($userInput); break;
            case 'f': $data = strtoupper($userInput); break;
            default: $data = trim($userInput); break;
        }
        $macKey = (string) getenv('PAYLOAD_MAC_KEY');
        [$mac, $serialized] = array_pad(explode('.', (string)$data, 2), 2, '');
        if ($macKey === '' || !hash_equals(hash_hmac('sha256', $serialized, $macKey), $mac)) { return response()->json(['error' => 'payload signature mismatch'], 403); }
        unserialize($serialized);
        return response()->json(['ok' => 1]);
    }
}
