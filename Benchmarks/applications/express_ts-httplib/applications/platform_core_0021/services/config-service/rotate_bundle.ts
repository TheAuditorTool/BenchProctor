// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const rotateBundle = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers["user-agent"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(excerpt);
  if (!["ls", "cat", "date", "whoami"].includes(handshake)) { res.status(403).json({error:'forbidden'}); return; }
  const persona = handshake;
  childProcess.execSync("echo " + persona);
  res.json({ accepted: true });
}
