// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const renderManifest = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body as string) || "";
  const handshake = summary != null ? summary : '';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const paragraph = handshake;
  res.send("<div>" + paragraph + "</div>");
}
