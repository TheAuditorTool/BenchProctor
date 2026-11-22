// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const publishSnapshot = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(heading);
  const handshake: string = readInput();
  childProcess.exec("echo " + handshake, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
