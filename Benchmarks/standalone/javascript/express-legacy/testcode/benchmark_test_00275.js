// SPDX-License-Identifier: Apache-2.0
const vm = require("node:vm");

async function BenchmarkTest00275(req, res) {
  const userInput = req.body.payload || "";
  vm.runInNewContext(String(userInput), { Math });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00275 };
