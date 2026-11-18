// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00035(req, res) {
  const userInput = req.query.id || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  res.json({ done: true });
}

module.exports = { BenchmarkTest00035 };
