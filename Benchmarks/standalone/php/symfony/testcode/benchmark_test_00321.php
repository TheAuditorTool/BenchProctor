<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00321', methods: ['POST'])]
class BenchmarkTest00321Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $transform = fn (string $v): string => trim($v);
        $data = $transform($userInput);
        $request->getSession()->set('data', (string) $data);
        return new JsonResponse(["committed" => true]);
    }
}
