// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00554 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00554 };
