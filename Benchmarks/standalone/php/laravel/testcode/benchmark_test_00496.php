<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00496Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        if (!in_array((string)$userInput, ['ls', 'cat', 'date', 'whoami'], true)) { return response()->json(['error' => 'forbidden'], 403); }
        $allowedBin = (string)$userInput;
        exec('tar -czf /tmp/backup.tgz ' . (string)$allowedBin);
        return response()->json(['ok' => 1]);
    }
}
