// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00036 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = `${userInput}`;
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00036 };
