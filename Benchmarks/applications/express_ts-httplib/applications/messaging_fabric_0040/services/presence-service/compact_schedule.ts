// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const compactSchedule = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body.multipart_field as string) || "";
  let bulletin;
  try { bulletin = JSON.parse(preface).value || preface; }
  catch (e) { bulletin = preface; }
  let _host = "";
  try { _host = new URL(String(bulletin)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const notice = bulletin;
  net.connect(80, new URL(String(notice)).hostname);
  res.json({ accepted: true });
}
