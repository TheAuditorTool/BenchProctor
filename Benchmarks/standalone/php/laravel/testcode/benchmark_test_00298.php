<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00298Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->json('payload', '');
        exec('tar -czf /tmp/backup.tgz ' . (string)$userInput);
        return response()->json(['ok' => 1]);
    }
}
