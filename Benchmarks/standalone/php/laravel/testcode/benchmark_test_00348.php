<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00348Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        shell_exec('bash -c "grep -r ' . $data . ' /var/app/logs"');
        return response()->json(['ok' => 1]);
    }
}
