// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00332 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00332 };
