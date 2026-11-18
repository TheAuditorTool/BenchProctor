<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00634', methods: ['POST'])]
class BenchmarkTest00634Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        unserialize($data);
        return new JsonResponse(["committed" => true]);
    }
}
