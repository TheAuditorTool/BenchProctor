// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

const BenchmarkTest00582 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  nodeSerialize.unserialize(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00582 };
