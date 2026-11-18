<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00376', methods: ['POST'])]
class BenchmarkTest00376Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $data = "{$userInput}";
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        $resolved = gethostbyname($host);
        if (preg_match('#^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)#', $resolved)) { return new JsonResponse(['error' => 'private range blocked'], 403); }
        $targetUrl = $data;
        $errno = 0; $errstr = '';
        fsockopen((string)$targetUrl, 80, $errno, $errstr, 30);
        return new JsonResponse(["committed" => true]);
    }
}
