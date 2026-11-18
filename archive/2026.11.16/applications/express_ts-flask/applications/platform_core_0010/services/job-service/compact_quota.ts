// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const compactQuota = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.headers.referer as string) || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(notice);
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const handshake = persona;
  childProcess.execSync("echo " + handshake);
  res.json({ accepted: true });
}
