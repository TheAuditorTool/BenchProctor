// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function exportRoster(req, res) {
  const tagline = req.headers.host || "";
  const persona = `${tagline}`;
  http.get(persona);
  res.json({ done: true });
}

module.exports = { exportRoster };
