// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

async function BenchmarkTest00610(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const data = String(userInput).replace(/\u0000/g, "");
  nodeSerialize.unserialize(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00610 };
