// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00476 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  ctx.redirect(userInput);
}

module.exports = { BenchmarkTest00476 };
