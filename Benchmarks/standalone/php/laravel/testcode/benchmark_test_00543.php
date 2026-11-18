<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00543Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $data = ($userInput !== null) ? $userInput : '';
        if (!in_array((string)$data, ['ls', 'cat', 'date', 'whoami'], true)) { return response()->json(['error' => 'forbidden'], 403); }
        $allowedBin = (string)$data;
        shell_exec('bash -c "grep -r ' . $allowedBin . ' /var/app/logs"');
        return response()->json(['ok' => 1]);
    }
}
