// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const buildWindow = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers["user-agent"] as string) || "";
  let _host = "";
  try { _host = new URL(String(remark)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const notice = remark;
  http.get(notice);
  res.json({ accepted: true });
}
