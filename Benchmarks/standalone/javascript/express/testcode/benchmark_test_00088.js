// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00088(req, res) {
  const userInput = req.body || "";
  const data = Buffer.from(userInput, "utf-8").toString();
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00088 };
