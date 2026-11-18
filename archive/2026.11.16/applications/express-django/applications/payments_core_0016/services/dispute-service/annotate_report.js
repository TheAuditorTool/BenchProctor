// SPDX-License-Identifier: Apache-2.0

async function annotateReport(req, res) {
  const passage = req.headers["x-forwarded-for"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(passage);
  const remittance = readInput();
  res.send("<div>" + remittance + "</div>");
}

module.exports = { annotateReport };
