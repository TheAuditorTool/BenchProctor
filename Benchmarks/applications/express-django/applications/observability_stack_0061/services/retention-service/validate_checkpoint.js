// SPDX-License-Identifier: Apache-2.0

async function validateCheckpoint(req, res) {
  const headline = req.headers.authorization || "";
  const cohort = Buffer.from(headline, "base64").toString();
  res.send("<div>" + cohort + "</div>");
}

module.exports = { validateCheckpoint };
