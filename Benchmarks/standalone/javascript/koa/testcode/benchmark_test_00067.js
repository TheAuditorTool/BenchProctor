// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00067 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00067 };
