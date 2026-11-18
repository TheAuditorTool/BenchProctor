// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const validateSchedule = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.body.multipart_field as string) || "";
  let bulletin;
  try { bulletin = JSON.parse(subject).value || subject; }
  catch (e) { bulletin = subject; }
  let _host = "";
  try { _host = new URL(String(bulletin)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const passage = bulletin;
  net.connect(80, new URL(String(passage)).hostname);
  res.json({ accepted: true });
}
