// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const annotateWindow = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.body?.payload as string) || "";
  const persona = subtitle != null ? subtitle : '';
  childProcess.execFile("echo", [String(persona)], (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
