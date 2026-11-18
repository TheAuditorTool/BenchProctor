// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function BenchmarkTest00099(req, res) {
  const userInput = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  const data = userInput != null ? userInput : '';
  nodeSerialize.unserialize(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00099 };
