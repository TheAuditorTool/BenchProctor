<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00298Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        shell_exec('bash -c "grep -r ' . $data . ' /var/app/logs"');
        return response()->json(['ok' => 1]);
    }
}
