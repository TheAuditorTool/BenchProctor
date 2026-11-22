// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const vm = require("node:vm");

async function BenchmarkTest00269(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  vm.runInNewContext(String(processed), { Math });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00269 };
