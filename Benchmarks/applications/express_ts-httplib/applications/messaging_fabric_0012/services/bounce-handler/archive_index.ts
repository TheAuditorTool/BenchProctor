// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const archiveIndex = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body?.payload as string) || "";
  const bulletin = preface != null ? preface : '';
  childProcess.execFile("echo", [String(bulletin)], (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
