<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00087Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookie('session_token', '');
        $data = hex2bin($userInput);
        $quotedArg = escapeshellarg((string)$data);
        exec('tar -czf /tmp/backup.tgz ' . (string)$quotedArg);
        return response()->json(['ok' => 1]);
    }
}
