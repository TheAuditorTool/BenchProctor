// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const renderReceipt = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.body?.payload as string) || "";
  const persona = tagline != null ? tagline : '';
  childProcess.execFile("echo", [String(persona)], (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
