// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00378 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = String(userInput).split(/[ \t]+/).join(" ");
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00378 };
