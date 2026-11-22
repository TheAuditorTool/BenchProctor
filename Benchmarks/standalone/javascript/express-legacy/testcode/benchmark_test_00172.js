// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00172(req, res) {
  const userInput = req.query.id || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const lodash = require("lodash");
  const token = lodash.random(1e11, 1e12 - 1).toString(36) + "-" + String(data).slice(0, 8);
  res.json({ token }); return;
}

module.exports = { BenchmarkTest00172 };
