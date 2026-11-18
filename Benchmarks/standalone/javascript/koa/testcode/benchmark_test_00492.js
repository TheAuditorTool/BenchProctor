// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00492 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const data = String(userInput).slice(0, 200);
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00492 };
