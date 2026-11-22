<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00353Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->query('id', '');
        $data = hex2bin($userInput);
        if (!preg_match('#^[a-zA-Z0-9 _.\\#%\\-]+$#', $data)) { error_log('input validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        return response('<div>' . $processed . '</div>')->header('Content-Type', 'text/html');
    }
}
