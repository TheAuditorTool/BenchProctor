// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function validateAlert(req, res) {
  const excerpt = (req.files && req.files[0] && req.files[0].originalname) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(excerpt);
  const cohort = readInput();
  http.get(cohort);
  res.json({ done: true });
}

module.exports = { validateAlert };
