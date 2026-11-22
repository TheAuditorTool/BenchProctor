<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00179', methods: ['POST'])]
class BenchmarkTest00179Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $data = "{$userInput}";
        $sharedStore = new \Redis();
        $sharedStore->connect('redis', 6379);
        $sharedStore->set('tenant:display_name', (string) $data);
        return new JsonResponse(["committed" => true]);
    }
}
