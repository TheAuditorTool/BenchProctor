<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00451Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT bio FROM profiles LIMIT 1')->bio;
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        unlink('/var/app/data/' . $data);
        return response()->json(['ok' => 1]);
    }
}
