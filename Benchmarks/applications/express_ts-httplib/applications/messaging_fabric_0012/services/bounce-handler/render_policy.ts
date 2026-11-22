// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const renderPolicy = async (req: Request, res: Response): Promise<void> => {
  const preface = process.env.MESSAGING_INPUT_0012 || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const bulletin: string = normalize(preface);
  childProcess.spawn("echo " + bulletin, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
