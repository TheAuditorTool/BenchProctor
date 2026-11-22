// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00307(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  if (!/^[a-zA-Z0-9 _.\-]+$/.test(userInput)) { res.status(400).json({error:"invalid"}); return; }
  const processed = userInput;
  Object.assign(req.session, { data: String(processed), expiresAt: Date.now() + 900000 });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00307 };
