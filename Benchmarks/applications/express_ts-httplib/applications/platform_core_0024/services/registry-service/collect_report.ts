// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const collectReport = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.body?.payload as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(heading);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const persona = handshake;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + persona + "</section>"); return;
}
