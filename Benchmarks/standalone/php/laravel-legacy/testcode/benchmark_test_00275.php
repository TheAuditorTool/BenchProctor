<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00275Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $data = sprintf('%s', $userInput);
        $macKey = (string) getenv('PAYLOAD_MAC_KEY');
        [$mac, $serialized] = array_pad(explode('.', (string)$data, 2), 2, '');
        if ($macKey === '' || !hash_equals(hash_hmac('sha256', $serialized, $macKey), $mac)) { return response()->json(['error' => 'payload signature mismatch'], 403); }
        unserialize($serialized);
        return response()->json(['ok' => 1]);
    }
}
