// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00468 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [data] });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00468 };
