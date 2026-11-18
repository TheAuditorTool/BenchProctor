// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00205(req, res) {
  const userInput = req.body.field || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00205 };
