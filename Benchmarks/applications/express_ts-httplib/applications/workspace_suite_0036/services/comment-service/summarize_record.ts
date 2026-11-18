// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const summarizeRecord = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers["user-agent"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const synopsis: string = normalize(remark);
  if (!["ls", "cat", "date", "whoami"].includes(synopsis)) { res.status(403).json({error:'forbidden'}); return; }
  const quotation = synopsis;
  childProcess.execSync("echo " + quotation);
  res.json({ accepted: true });
}
