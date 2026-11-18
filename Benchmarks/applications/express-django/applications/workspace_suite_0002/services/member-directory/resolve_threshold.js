// SPDX-License-Identifier: Apache-2.0

async function resolveThreshold(req, res) {
  const transcript = req.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const heading = trim(transcript);
  res.send("<div>" + heading + "</div>");
}

module.exports = { resolveThreshold };
