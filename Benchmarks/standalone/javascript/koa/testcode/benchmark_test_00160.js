// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00160 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = Buffer.from(userInput, "base64").toString();
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00160 };
