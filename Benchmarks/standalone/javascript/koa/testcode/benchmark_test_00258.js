// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const vm = require("node:vm");

const BenchmarkTest00258 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  vm.runInNewContext(String(processed), { Math });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00258 };
