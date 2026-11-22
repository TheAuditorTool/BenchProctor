// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const publishConfig = async (req: Request, res: Response): Promise<void> => {
  const headline = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const backorder = headline != null ? headline : '';
  let _host = "";
  try { _host = new URL(String(backorder)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const voucher = backorder;
  http.get(voucher);
  res.json({ accepted: true });
}
