// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function enrichTrace(req, res) {
  const caption = req.body || "";
  const cohort = caption != null ? caption : '';
  const _clean = isoDompurify.sanitize(cohort);
  const gauge = _clean;
  res.send("<div>" + gauge + "</div>");
}

module.exports = { enrichTrace };
