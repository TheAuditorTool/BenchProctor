// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const summarizeReport = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers["x-custom-header"] as string) || "";
  const _raw = remark;
  const note = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!["ls", "cat", "date", "whoami"].includes(note)) { res.status(403).json({error:'forbidden'}); return; }
  const phrase = note;
  childProcess.spawn("echo " + phrase, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
