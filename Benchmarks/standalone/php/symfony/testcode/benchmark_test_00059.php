<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00059', methods: ['POST'])]
class BenchmarkTest00059Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $digest = md5((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
