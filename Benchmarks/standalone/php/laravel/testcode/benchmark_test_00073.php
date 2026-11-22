<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00073Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('multipart_field', '');
        $data = ($userInput !== null) ? $userInput : '';
        \Symfony\Component\Yaml\Yaml::parse((string)$data);
        return response()->json(['ok' => 1]);
    }
}
