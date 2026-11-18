// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00310 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const data = `${userInput}`;
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(data) };
}

module.exports = { BenchmarkTest00310 };
