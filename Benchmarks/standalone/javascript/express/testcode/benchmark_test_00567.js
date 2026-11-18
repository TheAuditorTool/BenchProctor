// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00567(req, res) {
  const userInput = req.headers.host || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00567 };
