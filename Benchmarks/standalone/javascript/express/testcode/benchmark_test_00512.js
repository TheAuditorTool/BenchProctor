// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function BenchmarkTest00512(req, res) {
  const userInput = req.query.id || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  nodeSerialize.unserialize(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00512 };
