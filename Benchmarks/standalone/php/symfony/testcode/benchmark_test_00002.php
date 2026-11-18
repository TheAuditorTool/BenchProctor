<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/BenchmarkTest00002', methods: ['POST'])]
class BenchmarkTest00002Controller
{
    public function __invoke(Request $request)
    {
        $userInput = $request->getContent();
        $pending = explode(',', $userInput);
        $data = '';
        while (count($pending)) { $data = array_shift($pending); }
        $ldap = ldap_connect(getenv('LDAP_URL') ?: 'ldap://directory:1389');
        ldap_set_option($ldap, LDAP_OPT_PROTOCOL_VERSION, 3);
        ldap_bind($ldap, getenv('LDAP_BIND_DN'), getenv('LDAP_BIND_PASS'));
        $entries = ldap_search($ldap, 'ou=people,dc=example,dc=com', '(uid=' . $data . ')');
        return new JsonResponse(["committed" => true]);
    }
}
