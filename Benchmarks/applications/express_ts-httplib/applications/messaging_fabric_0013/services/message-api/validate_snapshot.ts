// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const validateSnapshot = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers["user-agent"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const bulletin: string = normalize(summary);
  if (!["ls", "cat", "date", "whoami"].includes(bulletin)) { res.status(403).json({error:'forbidden'}); return; }
  const snippet = bulletin;
  childProcess.execSync("echo " + snippet);
  res.json({ accepted: true });
}
