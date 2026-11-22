// SPDX-License-Identifier: Apache-2.0
const vm = require("node:vm");

const BenchmarkTest00029 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  vm.runInNewContext(String(data), { Math });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00029 };
