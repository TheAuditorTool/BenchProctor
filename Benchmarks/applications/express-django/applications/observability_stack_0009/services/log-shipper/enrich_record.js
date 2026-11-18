// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function enrichRecord(req, res) {
  const summary = req.body || "";
  const gauge = summary != null ? summary : '';
  const _clean = isoDompurify.sanitize(gauge);
  const cohort = _clean;
  res.send("<div>" + cohort + "</div>");
}

module.exports = { enrichRecord };
