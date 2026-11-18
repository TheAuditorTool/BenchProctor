// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00011(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  await db.query("SELECT * FROM users ORDER BY " + processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00011 };
