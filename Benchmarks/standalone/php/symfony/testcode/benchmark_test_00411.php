<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00411', methods: ['POST'])]
class BenchmarkTest00411Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        $data = (!empty($userInput)) ? $userInput : '';
        eval((string)$data);
        return new JsonResponse(["committed" => true]);
    }
}
