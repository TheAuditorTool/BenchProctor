// SPDX-License-Identifier: Apache-2.0

async function verifySchedule(req, res) {
  const paragraph = req.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const bulletin = trim(paragraph);
  res.send("<div>" + bulletin + "</div>");
}

module.exports = { verifySchedule };
