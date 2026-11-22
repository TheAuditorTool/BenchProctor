// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const resolvePolicy = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body?.payload as string) || "";
  const rendition = citation != null ? citation : '';
  childProcess.execFile("echo", [String(rendition)], (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
