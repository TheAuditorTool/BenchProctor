<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00306Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $data = (!empty($userInput)) ? $userInput : '';
        if (!preg_match('#^(asc|desc|name|created)$#', (string)$data)) { error_log('enum validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        system('gzip -f /var/app/reports/' . (string)$processed);
        return response()->json(['ok' => 1]);
    }
}
