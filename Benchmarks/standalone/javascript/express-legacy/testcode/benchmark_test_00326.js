// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00326(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  if (!/^[a-zA-Z0-9 _.\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  req.app.locals.announcement = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00326 };
