<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00203Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = base64_decode($userInput);
        $quotedArg = escapeshellarg((string)$data);
        system('gzip -f /var/app/reports/' . (string)$quotedArg);
        return response()->json(['ok' => 1]);
    }
}
