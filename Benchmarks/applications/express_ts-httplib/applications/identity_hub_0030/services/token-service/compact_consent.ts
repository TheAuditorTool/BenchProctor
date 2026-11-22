// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const compactConsent = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.headers["x-custom-header"] as string) || "";
  const _raw = tagline;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!["ls", "cat", "date", "whoami"].includes(persona)) { res.status(403).json({error:'forbidden'}); return; }
  const note = persona;
  childProcess.spawn("echo " + note, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
