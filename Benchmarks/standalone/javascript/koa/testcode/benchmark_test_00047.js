// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00047 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  crypto.createHash("md5").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00047 };
