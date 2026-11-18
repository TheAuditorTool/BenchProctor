<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00123Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->route('id') ?? $request->input('id', ''));
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        exec('tar -czf /tmp/backup.tgz ' . (string)$data);
        return response()->json(['ok' => 1]);
    }
}
