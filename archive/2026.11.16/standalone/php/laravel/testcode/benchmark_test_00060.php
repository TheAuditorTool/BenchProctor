<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00060Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = str_replace("\0", '', $userInput);
        if (!in_array((string)$data, ['ls', 'cat', 'date', 'whoami'], true)) { return response()->json(['error' => 'forbidden'], 403); }
        $allowedBin = (string)$data;
        exec('tar -czf /tmp/backup.tgz ' . (string)$allowedBin);
        return response()->json(['ok' => 1]);
    }
}
