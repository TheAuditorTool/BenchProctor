// SPDX-License-Identifier: Apache-2.0
const vm = require("node:vm");

async function BenchmarkTest00046(req, res) {
  const userInput = req.headers.origin || "";
  const data = String(userInput).replace(/\u0000/g, "");
  vm.runInNewContext(String(data), { Math });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00046 };
