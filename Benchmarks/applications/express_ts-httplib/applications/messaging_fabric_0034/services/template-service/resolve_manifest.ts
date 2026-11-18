// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const resolveManifest = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.multipart_field as string) || "";
  let bulletin;
  try { bulletin = JSON.parse(footnote).value || footnote; }
  catch (e) { bulletin = footnote; }
  let _host = "";
  try { _host = new URL(String(bulletin)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const heading = bulletin;
  net.connect(80, new URL(String(heading)).hostname);
  res.json({ accepted: true });
}
