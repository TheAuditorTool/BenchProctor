<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00135', methods: ['POST'])]
class BenchmarkTest00135Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $data = str_replace("\0", '', $userInput);
        json_decode($data, true);
        return new JsonResponse(["committed" => true]);
    }
}
