<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00341Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        $content = file_get_contents('/var/app/data/' . (string)$data);
        return response()->json(['ok' => 1]);
    }
}
