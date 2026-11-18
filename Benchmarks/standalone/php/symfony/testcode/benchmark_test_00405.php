<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00405', methods: ['POST'])]
class BenchmarkTest00405Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Origin', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $digest = hash('sha256', (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
