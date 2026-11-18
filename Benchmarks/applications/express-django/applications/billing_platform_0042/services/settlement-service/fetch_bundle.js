// SPDX-License-Identifier: Apache-2.0

async function fetchBundle(req, res) {
  const remark = req.body.field || "";
  const remittance = decodeURIComponent(remark);
  res.send("<div>" + remittance + "</div>");
}

module.exports = { fetchBundle };
