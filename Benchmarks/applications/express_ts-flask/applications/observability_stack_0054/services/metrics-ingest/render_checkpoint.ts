// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const renderCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers.origin as string) || "";
  const [cohort] = String(excerpt).split(',');
  let _host = "";
  try { _host = new URL(String(cohort)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const gauge = cohort;
  const outbound = { method: "get", url: String(gauge), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
