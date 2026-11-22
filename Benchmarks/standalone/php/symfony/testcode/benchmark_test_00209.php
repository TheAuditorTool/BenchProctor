<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Validator\Validation;
use Symfony\Component\Validator\Constraints as Assert;

#[Route('/BenchmarkTest00209', methods: ['POST'])]
class BenchmarkTest00209Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Origin', '');
        $tokens = explode(',', $userInput);
        $data = implode(' ', $tokens);
        $_violations = Validation::createValidator()->validate((string)$data, [new Assert\Regex(pattern: '#^[a-zA-Z0-9 _.\\-]+$#')]);
        if (count($_violations) > 0) { error_log('schema validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = (string)$data;
        $session = $request->getSession();
        $session->replace(array_merge($session->all(), ['data' => (string) $processed, 'data_updated_at' => time()]));
        return new JsonResponse(["committed" => true]);
    }
}
