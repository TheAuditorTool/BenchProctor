// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00239(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00239 };
