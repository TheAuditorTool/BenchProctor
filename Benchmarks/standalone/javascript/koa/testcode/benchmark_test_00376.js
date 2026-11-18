// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00376 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00376 };
