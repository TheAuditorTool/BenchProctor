<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00064', methods: ['POST'])]
class BenchmarkTest00064Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['variables']['input'] ?? '';
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        $_coerced = max(0, min((int)$data, 1048576));
        $boundedVal = $_coerced;
        $quantity = (int) $boundedVal;
        $lineTotal = intval($quantity * 1999);
        return new JsonResponse(['line_total_cents' => $lineTotal], 200);
    }
}
