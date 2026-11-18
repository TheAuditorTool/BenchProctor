<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Validator\Validation;
use Symfony\Component\Validator\Constraints as Assert;

#[Route('/BenchmarkTest00205', methods: ['POST'])]
class BenchmarkTest00205Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->request->get('field', '');
        $thunk = function () use ($userInput) { return trim($userInput); };
        $data = $thunk();
        $_violations = Validation::createValidator()->validate((string)$data, [new Assert\Regex(['pattern' => '#^[a-zA-Z0-9 _.\\-]+$#'])]);
        if (count($_violations) > 0) { error_log('schema validation failed'); return new JsonResponse(['error'=>'invalid'], 400); }
        $processed = (string)$data;
        $request->getSession()->set('data', (string) $processed);
        return new JsonResponse(["committed" => true]);
    }
}
