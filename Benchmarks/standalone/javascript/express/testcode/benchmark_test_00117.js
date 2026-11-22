// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00117(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  return res.status(302).set("Location", String(data)).end();
}

module.exports = { BenchmarkTest00117 };
