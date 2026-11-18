// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function BenchmarkTest00537(req, res) {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const data = String(userInput).replace(/\u0000/g, "");
  nodeSerialize.unserialize(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00537 };
