// SPDX-License-Identifier: Apache-2.0

async function auditRecord(req, res) {
  const passage = req.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const dossier = trim(passage);
  res.send("<div>" + dossier + "</div>");
}

module.exports = { auditRecord };
