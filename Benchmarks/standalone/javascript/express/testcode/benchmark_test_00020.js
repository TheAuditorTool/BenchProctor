// SPDX-License-Identifier: Apache-2.0
const ldapjs = require("ldapjs");

async function BenchmarkTest00020(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.compare("uid=" + data + ",ou=people,dc=example,dc=com", "employeeType", "manager", (_err, _matched) => ldapClient.unbind());
  res.json({ done: true });
}

module.exports = { BenchmarkTest00020 };
