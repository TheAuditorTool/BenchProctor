// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const buildBundle = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers.origin as string) || "";
  const [byline] = String(synopsis).split(',');
  let _host = "";
  try { _host = new URL(String(byline)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const addendum = byline;
  const outbound = { method: "get", url: String(addendum), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
