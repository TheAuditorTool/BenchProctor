// SPDX-License-Identifier: Apache-2.0
const ldapjs = require("ldapjs");

const BenchmarkTest00197 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.compare("uid=" + userInput + ",ou=people,dc=example,dc=com", "employeeType", "manager", (_err, _matched) => ldapClient.unbind());
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00197 };
