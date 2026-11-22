<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00085Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        if (!preg_match('#^[a-zA-Z0-9 _.\\#~\\-]+$#', $userInput)) { error_log('input validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $userInput;
        file_put_contents('/var/uploads/' . $processed, 'data');
        return response()->json(['ok' => 1]);
    }
}
