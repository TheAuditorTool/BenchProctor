<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00082', methods: ['POST'])]
class BenchmarkTest00082Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->files->get('upload')?->getClientOriginalName() ?? '');
        $data = vsprintf('%1$s', [$userInput]);
        mt_srand(ctype_digit((string)$data) ? (int)$data : 42);
        $token = mt_rand();
        return new JsonResponse(['token' => (string)$token], 200);
    }
}
