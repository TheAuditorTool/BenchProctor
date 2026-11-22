<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00082', methods: ['POST'])]
class BenchmarkTest00082Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        $scheme = strtolower((string) parse_url($data, PHP_URL_SCHEME));
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!in_array($scheme, ['http', 'https'], true) || preg_match('/[\x00-\x20\\\\]/', (string) $data) || !preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return new JsonResponse(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        $response = new RedirectResponse('/account');
        $response->setTargetUrl((string)$targetUrl);
        return $response;
    }
}
