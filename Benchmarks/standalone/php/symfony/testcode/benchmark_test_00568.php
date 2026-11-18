<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00568', methods: ['POST'])]
class BenchmarkTest00568Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        $data = vsprintf('%1$s', [$userInput]);
        json_decode($data, true);
        return new JsonResponse(["committed" => true]);
    }
}
