<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00173Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        exec('tar -czf /tmp/backup.tgz ' . (string)$userInput);
        return response()->json(['ok' => 1]);
    }
}
