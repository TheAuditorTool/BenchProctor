<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00127', methods: ['POST'])]
class BenchmarkTest00127Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $form = new class($userInput) { public function __construct(public readonly string $payload) {} };
        $data = $form->payload;
        $scheme = strtolower((string) parse_url($data, PHP_URL_SCHEME));
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!in_array($scheme, ['http', 'https'], true) || preg_match('/[\x00-\x20\\\\]/', (string) $data) || !preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return new JsonResponse(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        $errno = 0; $errstr = '';
        fsockopen((string) parse_url((string)$targetUrl, PHP_URL_HOST), 80, $errno, $errstr, 30);
        return new JsonResponse(["committed" => true]);
    }
}
