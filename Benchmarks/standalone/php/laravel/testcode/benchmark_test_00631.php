<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00631Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        if (!preg_match('#^(asc|desc|name|created)$#', (string)$userInput)) { error_log('enum validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $userInput;
        return response('<div>' . $processed . '</div>')->header('Content-Type', 'text/html');
    }
}
