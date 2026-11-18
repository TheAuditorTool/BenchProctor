// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const collectProfile = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.body.payload as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const persona: string = normalize(notice);
  if (!/^(asc|desc|name|created)$/.test(String(persona))) { res.status(400).json({error:"invalid"}); return; }
  const handshake = persona;
  childProcess.execSync("echo " + handshake);
  res.json({ accepted: true });
}
