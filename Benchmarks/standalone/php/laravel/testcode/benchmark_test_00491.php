<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00491Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        shell_exec('bash -c "grep -r ' . $data . ' /var/app/logs"');
        return response()->json(['ok' => 1]);
    }
}
