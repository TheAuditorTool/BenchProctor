<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00164', methods: ['POST'])]
class BenchmarkTest00164Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->files->get('upload')?->getClientOriginalName() ?? '');
        $data = (!empty($userInput)) ? $userInput : '';
        $scheme = strtolower((string) parse_url($data, PHP_URL_SCHEME));
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!in_array($scheme, ['http', 'https'], true) || preg_match('/[\x00-\x20\\\\]/', (string) $data) || !preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return new JsonResponse(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        return new Response('', 302, ['Location' => (string)$targetUrl]);
    }
}
