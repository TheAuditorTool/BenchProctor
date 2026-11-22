<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00206Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $data = strtr('{0}', ['{0}' => (string)$userInput]);
        \Symfony\Component\Yaml\Yaml::parse((string)$data);
        return response()->json(['ok' => 1]);
    }
}
