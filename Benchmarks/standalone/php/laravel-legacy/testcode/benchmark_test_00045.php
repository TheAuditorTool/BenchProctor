<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00045Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        shell_exec('bash -c "grep -r ' . $data . ' /var/app/logs"');
        return response()->json(['ok' => 1]);
    }
}
