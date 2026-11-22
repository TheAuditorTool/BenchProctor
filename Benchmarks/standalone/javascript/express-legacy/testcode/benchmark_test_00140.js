// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function BenchmarkTest00140(req, res) {
  const userInput = req.headers.authorization || "";
  const data = `${userInput}`;
  nodeSerialize.unserialize(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00140 };
