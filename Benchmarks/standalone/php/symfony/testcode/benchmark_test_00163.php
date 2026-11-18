<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00163', methods: ['POST'])]
class BenchmarkTest00163Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['variables']['input'] ?? '';
        $data = vsprintf('%1$s', [$userInput]);
        $request->getSession()->set('data', (string) $data);
        return new JsonResponse(["committed" => true]);
    }
}
