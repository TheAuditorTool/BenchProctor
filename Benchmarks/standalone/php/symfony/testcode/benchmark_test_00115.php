<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00115', methods: ['POST'])]
class BenchmarkTest00115Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Host', '');
        $data = (!empty($userInput)) ? $userInput : '';
        eval((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
