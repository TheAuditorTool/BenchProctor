// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const enrichReport = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers["user-agent"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const rendition: string = normalize(transcript);
  if (!["ls", "cat", "date", "whoami"].includes(rendition)) { res.status(403).json({error:'forbidden'}); return; }
  const montage = rendition;
  childProcess.execSync("echo " + montage);
  res.json({ accepted: true });
}
