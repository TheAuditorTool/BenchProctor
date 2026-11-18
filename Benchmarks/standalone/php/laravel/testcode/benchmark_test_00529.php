<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00529Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $data = ($userInput !== null) ? $userInput : '';
        if (!preg_match('#^(asc|desc|name|created)$#', (string)$data)) { error_log('enum validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        shell_exec('bash -c "grep -r ' . $processed . ' /var/app/logs"');
        return response()->json(['ok' => 1]);
    }
}
