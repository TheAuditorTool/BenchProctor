// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00320(req, res) {
  const userInput = req.headers.referer || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const _desKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest().subarray(0, 24);
  crypto.createCipheriv("des-ede3-ecb", _desKey, null).update(String(data));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00320 };
