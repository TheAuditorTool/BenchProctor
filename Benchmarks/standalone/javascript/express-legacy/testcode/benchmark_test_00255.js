// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00255(req, res) {
  const userInput = req.cookies.session_token || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  res.json({ token });
}

module.exports = { BenchmarkTest00255 };
