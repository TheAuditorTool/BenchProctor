// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00107 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [data] });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00107 };
