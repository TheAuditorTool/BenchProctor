// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const enrichIndex = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.multipart_field as string) || "";
  let cohort;
  try { cohort = JSON.parse(summary).value || summary; }
  catch (e) { cohort = summary; }
  let _host = "";
  try { _host = new URL(String(cohort)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const gauge = cohort;
  net.connect(80, new URL(String(gauge)).hostname);
  res.json({ accepted: true });
}
