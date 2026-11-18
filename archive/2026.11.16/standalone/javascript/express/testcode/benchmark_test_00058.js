// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00058(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  res.json({ token });
}

module.exports = { BenchmarkTest00058 };
