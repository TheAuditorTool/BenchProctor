// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00350(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const data = nodeUtil.format("%s", userInput);
  req.app.locals.announcement = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00350 };
