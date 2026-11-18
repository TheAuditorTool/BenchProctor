<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00027', methods: ['POST'])]
class BenchmarkTest00027Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        eval((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
