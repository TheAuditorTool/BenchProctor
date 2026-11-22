// SPDX-License-Identifier: Apache-2.0
const ldapjs = require("ldapjs");

async function BenchmarkTest00171(req, res) {
  const userInput = req.headers.referer || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.compare("uid=" + data + ",ou=people,dc=example,dc=com", "employeeType", "manager", (_err, _matched) => ldapClient.unbind());
  res.json({ done: true });
}

module.exports = { BenchmarkTest00171 };
