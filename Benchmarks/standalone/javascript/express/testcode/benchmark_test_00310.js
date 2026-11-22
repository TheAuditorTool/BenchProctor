// SPDX-License-Identifier: Apache-2.0
const vm = require("node:vm");

async function BenchmarkTest00310(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  vm.runInNewContext(String(processed), { Math });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00310 };
