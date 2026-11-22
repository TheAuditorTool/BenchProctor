// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const buildReceipt = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers["user-agent"] as string) || "";
  let _host = "";
  try { _host = new URL(String(remark)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const phrase = remark;
  http.get(phrase);
  res.json({ accepted: true });
}
