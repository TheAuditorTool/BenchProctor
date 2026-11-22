<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00178', methods: ['POST'])]
class BenchmarkTest00178Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $data = ($userInput !== null) ? $userInput : '';
        file_get_contents((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
