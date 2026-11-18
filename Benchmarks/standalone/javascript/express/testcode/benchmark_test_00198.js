// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00198(req, res) {
  const userInput = req.params.id || "";
  const data = nodeUtil.format("%s", userInput);
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00198 };
