// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00040 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00040 };
