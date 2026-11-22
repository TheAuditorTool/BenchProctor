// SPDX-License-Identifier: Apache-2.0
const vm = require("node:vm");

async function BenchmarkTest00244(req, res) {
  const userInput = req.headers.authorization || "";
  const [data] = String(userInput).split(',');
  vm.runInNewContext(String(data), { Math });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00244 };
