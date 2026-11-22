<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00062Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        if (!preg_match('#^[a-zA-Z0-9 _.\\#~\\-]+$#', $data)) { error_log('input validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        $content = file_get_contents('/var/app/data/' . (string)$processed);
        return response()->json(['ok' => 1]);
    }
}
