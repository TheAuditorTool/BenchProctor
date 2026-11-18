// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const exportConfig = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers["user-agent"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const heading: string = normalize(transcript);
  if (!["ls", "cat", "date", "whoami"].includes(heading)) { res.status(403).json({error:'forbidden'}); return; }
  const passage = heading;
  childProcess.execSync("echo " + passage);
  res.json({ accepted: true });
}
