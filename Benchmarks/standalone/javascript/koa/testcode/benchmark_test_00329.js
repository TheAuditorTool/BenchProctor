// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00329 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = Buffer.from(userInput, "base64").toString();
  const quantity = parseInt(String(data), 10);
  const totalCents = Math.imul(quantity, 1999);
  ctx.body = { quantity, totalCents }; return;
}

module.exports = { BenchmarkTest00329 };
