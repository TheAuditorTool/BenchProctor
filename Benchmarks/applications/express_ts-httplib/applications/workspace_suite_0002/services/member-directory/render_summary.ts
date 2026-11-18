// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const renderSummary = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body.multipart_field as string) || "";
  let heading;
  try { heading = JSON.parse(transcript).value || transcript; }
  catch (e) { heading = transcript; }
  let _host = "";
  try { _host = new URL(String(heading)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const passage = heading;
  net.connect(80, new URL(String(passage)).hostname);
  res.json({ accepted: true });
}
