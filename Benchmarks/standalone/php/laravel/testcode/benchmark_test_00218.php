<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00218Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        $data = hex2bin($userInput);
        exec('tar -czf /tmp/backup.tgz ' . (string)$data);
        return response()->json(['ok' => 1]);
    }
}
