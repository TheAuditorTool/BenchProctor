// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00323(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  const _desKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest().subarray(0, 24);
  crypto.createCipheriv("des-ede3-ecb", _desKey, null).update(String(data));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00323 };
