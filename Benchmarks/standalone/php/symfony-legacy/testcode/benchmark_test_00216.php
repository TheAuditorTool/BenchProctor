<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00216', methods: ['POST'])]
class BenchmarkTest00216Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        system('gzip -f /var/app/reports/' . (string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
