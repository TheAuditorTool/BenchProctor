<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00086Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        if (!preg_match('#^[a-zA-Z0-9 _.\\#%\\-]+$#', $userInput)) { error_log('input validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $userInput;
        return response('<div>' . $processed . '</div>')->header('Content-Type', 'text/html');
    }
}
