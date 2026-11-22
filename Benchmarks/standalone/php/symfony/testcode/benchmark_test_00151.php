<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00151', methods: ['POST'])]
class BenchmarkTest00151Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Referer', '');
        $data = '';
        foreach (explode(',', $userInput) as $token) { $data = $token; }
        $compiled = tempnam('/var/app/cache', 'rule_');
        file_put_contents($compiled, '<?php return static fn (array $order) => ' . $data . ';');
        $rule = include $compiled;
        unlink($compiled);
        $result = $rule(['total' => 100, 'items' => 3]);
        return new JsonResponse(["committed" => true]);
    }
}
