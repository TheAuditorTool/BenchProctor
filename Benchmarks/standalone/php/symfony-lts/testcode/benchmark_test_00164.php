<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00164', methods: ['POST'])]
class BenchmarkTest00164Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        $checkedPath = '/var/app/data/' . basename($data);
        $content = file_get_contents($checkedPath);
        return new JsonResponse(["committed" => true]);
    }
}
