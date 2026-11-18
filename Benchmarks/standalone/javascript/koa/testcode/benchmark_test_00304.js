// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

const BenchmarkTest00304 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const data = String(userInput).replace(/\u0000/g, "");
  nodeSerialize.unserialize(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00304 };
