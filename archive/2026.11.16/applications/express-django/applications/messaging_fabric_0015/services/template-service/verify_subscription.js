// SPDX-License-Identifier: Apache-2.0

async function verifySubscription(req, res) {
  const heading = req.headers.authorization || "";
  const bulletin = Buffer.from(heading, "base64").toString();
  res.send("<div>" + bulletin + "</div>");
}

module.exports = { verifySubscription };
