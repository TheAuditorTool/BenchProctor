// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const annotateQuota = async (req: Request, res: Response): Promise<void> => {
  const note = process.env.PLATFORM_INPUT_0015 || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(note);
  childProcess.execSync("echo " + handshake);
  res.json({ accepted: true });
}
