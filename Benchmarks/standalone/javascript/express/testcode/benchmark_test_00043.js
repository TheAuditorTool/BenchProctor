// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00043(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const data = nodeUtil.format("%s", userInput);
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00043 };
