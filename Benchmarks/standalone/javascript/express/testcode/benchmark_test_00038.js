// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00038(req, res) {
  const userInput = req.body || "";
  const data = String(userInput).slice(0, 200);
  const lodash = require("lodash");
  const token = lodash.random(1e11, 1e12 - 1).toString(36) + "-" + String(data).slice(0, 8);
  res.json({ token }); return;
}

module.exports = { BenchmarkTest00038 };
