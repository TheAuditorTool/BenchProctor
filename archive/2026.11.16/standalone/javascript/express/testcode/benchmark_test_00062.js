// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00062(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00062 };
