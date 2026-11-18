// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00134(req, res) {
  const userInput = req.body.multipart_field || "";
  const data = `${userInput}`;
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00134 };
