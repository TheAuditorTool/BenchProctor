<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00010', methods: ['POST'])]
class BenchmarkTest00010Controller
{
    public function __invoke()
    {
        $userInput = file_get_contents('http://api.corp.lan/data');
        $data = (!empty($userInput)) ? $userInput : '';
        $host = parse_url($data, PHP_URL_HOST) ?: '';
        if (!preg_match('#^(api\\.corp\\.lan|cdn\\.shopcdn\\.io)$#', $host)) { return new JsonResponse(['error' => 'forbidden host'], 403); }
        $targetUrl = $data;
        return new RedirectResponse($targetUrl);
    }
}
