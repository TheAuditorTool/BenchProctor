// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00349(req, res) {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const data = String(userInput).replace(/\u0000/g, "");
  await db.query("SELECT * FROM users WHERE id = $1", [data]);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00349 };
