// SPDX-License-Identifier: Apache-2.0

async function collectManifest(req, res) {
  const heading = req.headers.authorization || "";
  const voucher = Buffer.from(heading, "base64").toString();
  res.send("<div>" + voucher + "</div>");
}

module.exports = { collectManifest };
