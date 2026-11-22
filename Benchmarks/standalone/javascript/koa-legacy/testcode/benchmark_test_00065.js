// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00065 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  const _desKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest().subarray(0, 24);
  crypto.createCipheriv("des-ede3-ecb", _desKey, null).update(String(data));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00065 };
