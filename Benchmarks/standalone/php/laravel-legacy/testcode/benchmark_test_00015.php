<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00015Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $data = "{$userInput}";
        if (!in_array((string)$data, ['ls', 'cat', 'date', 'whoami'], true)) { return response()->json(['error' => 'forbidden'], 403); }
        $allowedBin = (string)$data;
        shell_exec('bash -c "grep -r ' . $allowedBin . ' /var/app/logs"');
        return response()->json(['ok' => 1]);
    }
}
