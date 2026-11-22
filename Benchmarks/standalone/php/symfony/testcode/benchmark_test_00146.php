<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00146', methods: ['POST'])]
class BenchmarkTest00146Controller
{
    public function __invoke(Request $request)
    {
        $userInput = ($request->attributes->get('id') ?? $request->query->get('id', ''));
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        $session = $request->getSession();
        $session->replace(array_merge($session->all(), ['data' => (string) $data, 'data_updated_at' => time()]));
        return new JsonResponse(["committed" => true]);
    }
}
