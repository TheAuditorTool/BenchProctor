<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00031', methods: ['POST'])]
class BenchmarkTest00031Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('multipart_field', '');
        $data = ($userInput !== null) ? $userInput : '';
        $session = $request->getSession();
        $session->replace(array_merge($session->all(), ['data' => (string) $data, 'data_updated_at' => time()]));
        return new JsonResponse(["committed" => true]);
    }
}
