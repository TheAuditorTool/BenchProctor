<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00021Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        [$data] = [$userInput, 'http'];
        exec('tar -czf /tmp/backup.tgz ' . (string)$data);
        return response()->json(['ok' => 1]);
    }
}
