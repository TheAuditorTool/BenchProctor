<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00606', methods: ['POST'])]
class BenchmarkTest00606Controller
{
    public function __invoke()
    {
        $userInput = (new \Redis())->get('user_data');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return new JsonResponse(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        file_get_contents((string)$targetUrl);
        return new JsonResponse(["committed" => true]);
    }
}
