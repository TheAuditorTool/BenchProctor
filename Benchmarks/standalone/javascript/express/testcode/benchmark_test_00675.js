// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function BenchmarkTest00675(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  nodeSerialize.unserialize(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00675 };
