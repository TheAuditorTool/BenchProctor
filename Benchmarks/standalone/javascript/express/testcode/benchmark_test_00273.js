// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const nodeSerialize = require("node-serialize");

async function BenchmarkTest00273(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const data = nodeUtil.format("%s", userInput);
  nodeSerialize.unserialize(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00273 };
