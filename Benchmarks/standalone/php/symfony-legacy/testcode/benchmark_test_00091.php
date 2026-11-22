<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/BenchmarkTest00091', methods: ['POST'])]
class BenchmarkTest00091Controller
{
    public function __invoke(Request $request)
    {
        $userInput = json_decode($request->getContent(), true)['variables']['input'] ?? '';
        $payload = new class($userInput) { public function __construct(private string $raw) {} public function value(): string { return $this->raw; } };
        $data = $payload->value();
        $compiled = tempnam('/var/app/cache', 'rule_');
        file_put_contents($compiled, '<?php return static fn (array $order) => ' . $data . ';');
        $rule = include $compiled;
        unlink($compiled);
        $result = $rule(['total' => 100, 'items' => 3]);
        return new JsonResponse(["committed" => true]);
    }
}
