// SPDX-License-Identifier: Apache-2.0
const ldapjs = require("ldapjs");

const BenchmarkTest00562 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.search("ou=people,dc=example,dc=com", { filter: "(uid=" + data + ")", scope: "sub" }, (_err, _res) => (_res ? _res.on("end", () => ldapClient.unbind()).on("error", () => ldapClient.unbind()) : ldapClient.unbind()));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00562 };
