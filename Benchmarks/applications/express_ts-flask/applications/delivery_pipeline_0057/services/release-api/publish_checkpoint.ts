// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const publishCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.host as string) || "";
  const wording = `${footnote}`;
  let _host = "";
  try { _host = new URL(String(wording)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const note = wording;
  http.get(note);
  res.json({ accepted: true });
}
