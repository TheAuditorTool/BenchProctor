<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00693', methods: ['POST'])]
class BenchmarkTest00693Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['payload'] ?? '';
        $data = (!empty($userInput)) ? $userInput : '';
        $digest = md5((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
