// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function BenchmarkTest00140(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const data = String(userInput).slice(0, 200);
  nodeSerialize.unserialize(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00140 };
