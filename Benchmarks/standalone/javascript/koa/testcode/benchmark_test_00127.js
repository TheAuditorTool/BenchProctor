// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00127 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00127 };
