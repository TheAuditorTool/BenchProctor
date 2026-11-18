// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const verifyProfile = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.host as string) || "";
  const bulletin = `${heading}`;
  let _host = "";
  try { _host = new URL(String(bulletin)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const excerpt = bulletin;
  http.get(excerpt);
  res.json({ accepted: true });
}
