<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00073', methods: ['POST'])]
class BenchmarkTest00073Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        if (!preg_match('#^[a-zA-Z0-9 _.\\#~\\-]+$#', $userInput)) { error_log('input validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $userInput;
        file_put_contents('/var/uploads/' . $processed, 'data');
        return new JsonResponse(["committed" => true]);
    }
}
