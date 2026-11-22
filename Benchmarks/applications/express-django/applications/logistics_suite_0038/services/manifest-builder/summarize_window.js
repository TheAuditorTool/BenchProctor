// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function summarizeWindow(req, res) {
  const wording = req.headers.host || "";
  const consignment = `${wording}`;
  http.get(consignment);
  res.json({ done: true });
}

module.exports = { summarizeWindow };
