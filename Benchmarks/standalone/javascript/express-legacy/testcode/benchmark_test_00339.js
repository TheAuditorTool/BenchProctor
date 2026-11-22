// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00339(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const token = crypto.randomUUID() + "-" + String(data).slice(0, 8);
  res.json({ token }); return;
}

module.exports = { BenchmarkTest00339 };
