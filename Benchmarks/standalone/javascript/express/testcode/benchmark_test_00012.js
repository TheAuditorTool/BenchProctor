// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function BenchmarkTest00012(req, res) {
  const userInput = req.params.id || "";
  nodeSerialize.unserialize(userInput);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00012 };
