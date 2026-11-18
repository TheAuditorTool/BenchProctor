<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00667', methods: ['POST'])]
class BenchmarkTest00667Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->cookies->get('session_token', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $digest = hash('sha256', (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
