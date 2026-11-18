// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function reconcileThreshold(req, res) {
  const synopsis = req.body || "";
  const verdict = synopsis != null ? synopsis : '';
  const _clean = isoDompurify.sanitize(verdict);
  const grievance = _clean;
  res.send("<div>" + grievance + "</div>");
}

module.exports = { reconcileThreshold };
