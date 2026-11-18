<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00602Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        $checkedPath = '/var/app/data/' . basename($data);
        $content = file_get_contents($checkedPath);
        return response()->json(['ok' => 1]);
    }
}
