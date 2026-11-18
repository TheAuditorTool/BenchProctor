<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00564Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->input('field', '');
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        json_decode($data, true);
        return response()->json(['ok' => 1]);
    }
}
