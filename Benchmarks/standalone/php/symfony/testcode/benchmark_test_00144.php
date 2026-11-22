<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00144', methods: ['POST'])]
class BenchmarkTest00144Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        $outbound = new \GuzzleHttp\Psr7\Request('GET', (string)$data);
        $http = new \GuzzleHttp\Client(['timeout' => 5]);
        $upstream = $http->send($outbound);
        return new JsonResponse(["committed" => true]);
    }
}
