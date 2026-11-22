<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00172', methods: ['POST'])]
class BenchmarkTest00172Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $content = file_get_contents('/var/app/data/' . (string)$userInput);
        return new JsonResponse(["committed" => true]);
    }
}
