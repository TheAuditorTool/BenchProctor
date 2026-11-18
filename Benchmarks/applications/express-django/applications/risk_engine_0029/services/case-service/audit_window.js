// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function auditWindow(req, res) {
  const subject = req.body || "";
  const grievance = subject != null ? subject : '';
  const _clean = isoDompurify.sanitize(grievance);
  const verdict = _clean;
  res.send("<div>" + verdict + "</div>");
}

module.exports = { auditWindow };
