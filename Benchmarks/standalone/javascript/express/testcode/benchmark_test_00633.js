// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function BenchmarkTest00633(req, res) {
  const userInput = req.query.id || "";
  const data = String(userInput).slice(0, 200);
  nodeSerialize.unserialize(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00633 };
