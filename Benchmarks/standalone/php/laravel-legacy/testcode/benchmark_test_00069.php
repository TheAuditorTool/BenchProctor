<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00069Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('User-Agent', '');
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        unlink('/var/app/data/' . $data);
        return response()->json(['ok' => 1]);
    }
}
