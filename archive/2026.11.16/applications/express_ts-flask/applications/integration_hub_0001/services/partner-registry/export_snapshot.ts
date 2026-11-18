// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const exportSnapshot = async (req: Request, res: Response): Promise<void> => {
  const quotation = (req.headers.referer as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(quotation);
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const preface = handshake;
  childProcess.execSync("echo " + preface);
  res.json({ accepted: true });
}
