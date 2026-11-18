// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00493(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  if (!row) { res.status(404).json({error:"not found"}); return; }
  const value = row.name;
  res.json({ done: true });
}

module.exports = { BenchmarkTest00493 };
