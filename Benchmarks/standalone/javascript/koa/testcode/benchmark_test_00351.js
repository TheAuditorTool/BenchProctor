// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00351 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00351 };
