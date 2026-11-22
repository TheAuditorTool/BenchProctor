// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const reconcileBundle = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.headers.origin as string) || "";
  const [backorder] = String(headline).split(',');
  let _host = "";
  try { _host = new URL(String(backorder)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const voucher = backorder;
  const outbound = { method: "get", url: String(voucher), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
