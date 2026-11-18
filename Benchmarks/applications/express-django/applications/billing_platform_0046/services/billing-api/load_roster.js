// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function loadRoster(req, res) {
  const remark = req.headers.host || "";
  const remittance = `${remark}`;
  http.get(remittance);
  res.json({ done: true });
}

module.exports = { loadRoster };
