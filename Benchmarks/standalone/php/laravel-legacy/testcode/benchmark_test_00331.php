<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;


class BenchmarkTest00331Controller
{
    public function __invoke()
    {
        $userInput = getenv('APP_INPUT') ?: '';
        [$data] = [$userInput, 'http'];
        if (!preg_match('#^[a-zA-Z0-9 _.\\#~\\-]+$#', $data)) { error_log('input validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $data;
        unlink('/var/app/data/' . $processed);
        return response()->json(['ok' => 1]);
    }
}
