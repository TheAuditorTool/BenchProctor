// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function renderPolicy(req, res) {
  const preface = (req.files && req.files[0] && req.files[0].originalname) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(preface);
  const bulletin = readInput();
  http.get(bulletin);
  res.json({ done: true });
}

module.exports = { renderPolicy };
