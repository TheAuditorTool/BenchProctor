<?php
// SPDX-License-Identifier: Apache-2.0
namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;

class BenchmarkTest00163Controller
{
    public function __invoke()
    {
        $userInput = DB::selectOne('SELECT text FROM comments LIMIT 1')->text;
        if (!preg_match('#^[a-zA-Z0-9 _.\\#%\\-]+$#', $userInput)) { error_log('input validation failed'); return response()->json(['error'=>'invalid'], 400); }
        $processed = $userInput;
        $ldap = ldap_connect(getenv('LDAP_URL') ?: 'ldap://directory:1389');
        ldap_set_option($ldap, LDAP_OPT_PROTOCOL_VERSION, 3);
        ldap_bind($ldap, getenv('LDAP_BIND_DN'), getenv('LDAP_BIND_PASS'));
        $entries = ldap_list($ldap, 'ou=people,dc=example,dc=com', '(mail=' . $processed . ')', ['uid', 'cn']);
        return response()->json(['ok' => 1]);
    }
}
