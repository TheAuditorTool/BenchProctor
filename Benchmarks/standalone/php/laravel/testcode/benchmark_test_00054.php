<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00054Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Authorization', '');
        $data = vsprintf('%1$s', [$userInput]);
        $checkedPath = '/var/app/data/' . basename($data);
        unlink((string)$checkedPath);
        return response()->json(['ok' => 1]);
    }
}
