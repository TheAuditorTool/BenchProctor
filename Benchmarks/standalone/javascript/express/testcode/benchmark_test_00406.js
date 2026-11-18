// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00406(req, res) {
  const userInput = req.cookies.session_token || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  req.session.data = String(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00406 };
