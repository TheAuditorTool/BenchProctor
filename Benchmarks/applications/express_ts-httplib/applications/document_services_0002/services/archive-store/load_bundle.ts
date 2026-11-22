// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const loadBundle = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.body.payload as string) || "";
  const addendum = wording != null ? wording : '';
  childProcess.execFile("echo", [String(addendum)], (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
