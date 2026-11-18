<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00396', methods: ['POST'])]
class BenchmarkTest00396Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Host', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $request->getSession()->set('data', (string) $data);
        return new JsonResponse(["committed" => true]);
    }
}
