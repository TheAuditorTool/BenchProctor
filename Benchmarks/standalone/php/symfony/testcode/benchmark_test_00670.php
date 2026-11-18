<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00670', methods: ['POST'])]
class BenchmarkTest00670Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        [$data] = [$userInput, 'http'];
        $request->getSession()->set('data', (string) $data);
        return new JsonResponse(["committed" => true]);
    }
}
