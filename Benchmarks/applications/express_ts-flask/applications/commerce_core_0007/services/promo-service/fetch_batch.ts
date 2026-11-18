// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const fetchBatch = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.host as string) || "";
  const voucher = `${heading}`;
  let _host = "";
  try { _host = new URL(String(voucher)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const backorder = voucher;
  http.get(backorder);
  res.json({ accepted: true });
}
