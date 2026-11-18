<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00139', methods: ['POST'])]
class BenchmarkTest00139Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        $errno = 0; $errstr = '';
        fsockopen((string)$data, 80, $errno, $errstr, 30);
        return new JsonResponse(["committed" => true]);
    }
}
