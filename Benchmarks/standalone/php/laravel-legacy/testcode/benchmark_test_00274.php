<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BenchmarkTest00274Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->header('Origin', '');
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        $users = simplexml_load_file('/var/app/data/users.xml');
        $matches = $users->xpath("//user[@name='" . $data . "']");
        return response()->json(['ok' => 1]);
    }
}
