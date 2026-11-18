// SPDX-License-Identifier: Apache-2.0

async function auditReport(req, res) {
  const heading = req.headers.authorization || "";
  const _raw = heading;
  const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send("<div>" + consignment + "</div>");
}

module.exports = { auditReport };
