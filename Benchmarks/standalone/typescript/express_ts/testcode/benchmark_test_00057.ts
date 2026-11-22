// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00057 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const data: string = normalize(userInput);
  childProcess.spawn("echo " + data, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
