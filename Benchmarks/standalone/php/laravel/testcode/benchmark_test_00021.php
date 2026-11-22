<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00021Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        shell_exec('bash -c "grep -r ' . $data . ' /var/app/logs"');
        return response()->json(['ok' => 1]);
    }
}
