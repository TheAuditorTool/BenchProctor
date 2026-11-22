// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00083(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const [data] = String(userInput).split(',');
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00083 };
