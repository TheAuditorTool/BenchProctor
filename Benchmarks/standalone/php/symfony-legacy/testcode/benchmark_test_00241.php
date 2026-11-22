<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00241', methods: ['POST'])]
class BenchmarkTest00241Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        $data = vsprintf('%1$s', [$userInput]);
        if (!preg_match('#^(asc|desc|name|created)$#', (string)$data)) { error_log('enum validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = $data;
        $stream = function () use ($processed) {
            echo '<div class="comment">' . $processed . '</div>';
        };
        return new \Symfony\Component\HttpFoundation\StreamedResponse($stream, 200, ['Content-Type' => 'text/html']);
    }
}
