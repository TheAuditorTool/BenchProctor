// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00180 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00180 };
