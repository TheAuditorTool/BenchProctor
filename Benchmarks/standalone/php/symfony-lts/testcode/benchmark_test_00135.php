<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Doctrine\DBAL\Connection;

#[Route('/BenchmarkTest00135', methods: ['POST'])]
class BenchmarkTest00135Controller
{
    public function __invoke(Connection $conn)
    {
        $userInput = $conn->fetchOne('SELECT body FROM mq_messages ORDER BY id DESC LIMIT 1');
        try { $data = json_decode($userInput, true, 512, JSON_THROW_ON_ERROR)['value'] ?? $userInput; }
        catch (\JsonException $e) { $data = $userInput; }
        $scheme = strtolower((string) parse_url($data, PHP_URL_SCHEME));
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!in_array($scheme, ['http', 'https'], true) || preg_match('/[\x00-\x20\\\\]/', (string) $data) || !preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return new JsonResponse(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        $outbound = new \GuzzleHttp\Psr7\Request('GET', (string)$targetUrl);
        $http = new \GuzzleHttp\Client(['timeout' => 5]);
        $upstream = $http->send($outbound);
        return new JsonResponse(["committed" => true]);
    }
}
