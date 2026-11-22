<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00232', methods: ['POST'])]
class BenchmarkTest00232Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('multipart_field', '');
        $words = preg_split('/\s+/', $userInput);
        $data = implode(' ', $words);
        $hashCtx = hash_init('md4');
        hash_update($hashCtx, (string)$data);
        $digest = hash_final($hashCtx);
        return new JsonResponse(["committed" => true]);
    }
}
