// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00302(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00302 };
