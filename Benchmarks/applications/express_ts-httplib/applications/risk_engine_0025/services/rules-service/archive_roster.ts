// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const archiveRoster = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.body.payload as string) || "";
  const verdict = excerpt != null ? excerpt : '';
  childProcess.execFile("echo", [String(verdict)], (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
