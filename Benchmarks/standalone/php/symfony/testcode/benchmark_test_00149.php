<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00149', methods: ['POST'])]
class BenchmarkTest00149Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->headers->get('Authorization', '');
        $_coerced = in_array(strtolower((string)$userInput), ['true', '1', 'yes', 'on'], true) ? 'true' : 'false';
        $parsedBool = $_coerced;
        $compiled = tempnam('/var/app/cache', 'rule_');
        file_put_contents($compiled, '<?php return static fn (array $order) => ' . $parsedBool . ';');
        $rule = include $compiled;
        unlink($compiled);
        $result = $rule(['total' => 100, 'items' => 3]);
        return new JsonResponse(["committed" => true]);
    }
}
