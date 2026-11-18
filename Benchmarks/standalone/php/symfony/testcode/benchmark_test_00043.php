<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00043', methods: ['POST'])]
class BenchmarkTest00043Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('X-Custom-Header', '');
        $asText = function ($v): string { return trim((string) $v); };
        $data = $asText($userInput);
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return new JsonResponse(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        return new RedirectResponse($targetUrl);
    }
}
