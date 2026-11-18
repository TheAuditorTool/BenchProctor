// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00655 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00655 };
