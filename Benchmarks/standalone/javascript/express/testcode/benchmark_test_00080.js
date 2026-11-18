// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function BenchmarkTest00080(req, res) {
  const userInput = req.query.id || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  nodeSerialize.unserialize(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00080 };
