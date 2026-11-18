<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00278', methods: ['POST'])]
class BenchmarkTest00278Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Custom-Header', '');
        $digest = md5((string)$userInput);
        return new JsonResponse(["committed" => true]);
    }
}
