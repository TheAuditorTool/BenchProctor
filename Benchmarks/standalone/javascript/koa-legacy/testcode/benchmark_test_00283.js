// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00283 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = userInput != null ? userInput : '';
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00283 };
