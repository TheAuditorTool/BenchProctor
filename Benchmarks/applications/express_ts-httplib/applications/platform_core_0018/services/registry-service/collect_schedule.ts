// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const collectSchedule = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.headers["x-custom-header"] as string) || "";
  const _raw = subtitle;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!["ls", "cat", "date", "whoami"].includes(persona)) { res.status(403).json({error:'forbidden'}); return; }
  const handshake = persona;
  childProcess.spawn("echo " + handshake, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
