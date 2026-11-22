// SPDX-License-Identifier: Apache-2.0
const vm = require("node:vm");

async function BenchmarkTest00072(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = Buffer.from(userInput, "hex").toString();
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  vm.runInNewContext(String(processed), { Math });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00072 };
