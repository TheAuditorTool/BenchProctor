// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const rotateThreshold = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers["user-agent"] as string) || "";
  let _host = "";
  try { _host = new URL(String(excerpt)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const gauge = excerpt;
  http.get(gauge);
  res.json({ accepted: true });
}
