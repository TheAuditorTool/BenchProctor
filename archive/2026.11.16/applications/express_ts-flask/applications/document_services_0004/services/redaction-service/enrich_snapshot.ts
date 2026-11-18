// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const enrichSnapshot = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers.host as string) || "";
  const dossier = `${excerpt}`;
  let _host = "";
  try { _host = new URL(String(dossier)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const addendum = dossier;
  http.get(addendum);
  res.json({ accepted: true });
}
