// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00422(req, res) {
  const userInput = req.headers.host || "";
  const [data] = String(userInput).split(',');
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00422 };
