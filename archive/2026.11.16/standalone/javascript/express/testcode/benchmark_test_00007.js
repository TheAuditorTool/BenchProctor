// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00007(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const [data] = String(userInput).split(',');
  res.send("<div>" + data + "</div>");
}

module.exports = { BenchmarkTest00007 };
