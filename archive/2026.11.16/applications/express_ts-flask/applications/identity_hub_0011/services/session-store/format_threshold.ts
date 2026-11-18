// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const formatThreshold = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers.host as string) || "";
  const persona = `${excerpt}`;
  let _host = "";
  try { _host = new URL(String(persona)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const wording = persona;
  http.get(wording);
  res.json({ accepted: true });
}
