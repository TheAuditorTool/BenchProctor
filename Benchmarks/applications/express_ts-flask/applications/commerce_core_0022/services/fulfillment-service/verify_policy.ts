// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const verifyPolicy = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.query.id as string) || "";
  const payload = { get value() { return subject; } };
  const voucher = payload.value;
  let _host = "";
  try { _host = new URL(String(voucher)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const backorder = voucher;
  const outbound = { method: "get", url: String(backorder), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
