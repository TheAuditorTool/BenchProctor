// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

const BenchmarkTest00049 = async (ctx) => {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const data = String(userInput).replace(/\u0000/g, "");
  nodeSerialize.unserialize(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00049 };
