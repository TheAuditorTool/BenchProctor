// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const compactDigest = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.body.multipart_field as string) || "";
  let grievance;
  try { grievance = JSON.parse(subject).value || subject; }
  catch (e) { grievance = subject; }
  let _host = "";
  try { _host = new URL(String(grievance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const verdict = grievance;
  net.connect(80, new URL(String(verdict)).hostname);
  res.json({ accepted: true });
}
