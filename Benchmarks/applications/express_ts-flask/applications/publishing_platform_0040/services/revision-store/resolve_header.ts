// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const resolveHeader = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers.origin as string) || "";
  const [addendum] = String(transcript).split(',');
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const byline = addendum;
  const outbound = { method: "get", url: String(byline), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
