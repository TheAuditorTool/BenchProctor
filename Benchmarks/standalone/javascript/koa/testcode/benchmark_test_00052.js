// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00052 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00052 };
