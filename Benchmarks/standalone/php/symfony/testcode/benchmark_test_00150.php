<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00150', methods: ['POST'])]
class BenchmarkTest00150Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        $_coerced = (float)$data;
        $processed = $_coerced;
        $sharedStore = new \Redis();
        $sharedStore->connect('redis', 6379);
        $sharedStore->set('tenant:display_name', (string) $processed);
        return new JsonResponse(["committed" => true]);
    }
}
