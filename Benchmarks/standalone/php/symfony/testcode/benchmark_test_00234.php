<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00234', methods: ['POST'])]
class BenchmarkTest00234Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $_coerced = max(0, min((int)$data, 1048576));
        $boundedVal = $_coerced;
        $requested = (int) $boundedVal;
        $allocated = $requested + 1;
        return new JsonResponse(['allocated' => $allocated], 200);
    }
}
