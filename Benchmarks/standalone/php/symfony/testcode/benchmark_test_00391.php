<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00391', methods: ['POST'])]
class BenchmarkTest00391Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Custom-Header', '');
        $data = vsprintf('%1$s', [$userInput]);
        eval((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
