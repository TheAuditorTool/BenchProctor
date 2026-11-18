// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00079 = async (ctx) => {
  const userInput = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [data] });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00079 };
