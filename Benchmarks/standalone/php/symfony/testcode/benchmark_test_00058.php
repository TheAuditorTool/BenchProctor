<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00058', methods: ['POST'])]
class BenchmarkTest00058Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $request->getSession()->set('data', (string) $data);
        return new JsonResponse(["committed" => true]);
    }
}
