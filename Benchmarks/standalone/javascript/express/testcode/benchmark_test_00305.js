// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00305(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00305 };
