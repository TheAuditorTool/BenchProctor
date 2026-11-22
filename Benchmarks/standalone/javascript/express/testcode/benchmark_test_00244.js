// SPDX-License-Identifier: Apache-2.0
const vm = require("node:vm");

async function BenchmarkTest00244(req, res) {
  const userInput = process.env.APP_INPUT || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  vm.runInNewContext(String(data), { Math });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00244 };
