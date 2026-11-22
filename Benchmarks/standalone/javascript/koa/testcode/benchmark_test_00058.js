// SPDX-License-Identifier: Apache-2.0
const vm = require("node:vm");

const BenchmarkTest00058 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  const data = String(userInput).replace(/\u0000/g, "");
  vm.runInNewContext(String(data), { Math });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00058 };
