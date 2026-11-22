// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const ldapjs = require("ldapjs");

async function BenchmarkTest00059(req, res) {
  const userInput = req.body.field || "";
  const data = nodeUtil.format("%s", userInput);
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.compare("uid=" + data + ",ou=people,dc=example,dc=com", "employeeType", "manager", (_err, _matched) => ldapClient.unbind());
  res.json({ done: true });
}

module.exports = { BenchmarkTest00059 };
