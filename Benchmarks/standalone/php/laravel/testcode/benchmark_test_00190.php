<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00190Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->route('id') ?? $request->input('id', ''));
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        $content = file_get_contents('/var/app/data/' . (string)$data);
        return response()->json(['ok' => 1]);
    }
}
