// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00017 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00017 };
