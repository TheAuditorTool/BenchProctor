// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00178(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = userInput != null ? userInput : '';
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  req.app.locals.announcement = String(parsedNum);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00178 };
