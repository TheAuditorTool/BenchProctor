<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00353Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        return redirect($data);
    }
}
