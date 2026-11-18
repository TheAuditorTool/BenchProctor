// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function archiveSurvey(req, res) {
  const citation = req.headers.host || "";
  const grievance = `${citation}`;
  http.get(grievance);
  res.json({ done: true });
}

module.exports = { archiveSurvey };
