// SPDX-License-Identifier: Apache-2.0
const vm = require("node:vm");

const BenchmarkTest00029 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const [data] = String(userInput).split(',');
  vm.runInNewContext(String(data), { Math });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00029 };
