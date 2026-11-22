<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00026', methods: ['POST'])]
class BenchmarkTest00026Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $digest = sha1((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
