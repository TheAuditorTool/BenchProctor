// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00021(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const data = String(userInput).slice(0, 200);
  const token = crypto.randomInt(2 ** 47).toString(36) + crypto.randomInt(2 ** 47).toString(36) + "-" + String(data).slice(0, 8);
  res.json({ token }); return;
}

module.exports = { BenchmarkTest00021 };
