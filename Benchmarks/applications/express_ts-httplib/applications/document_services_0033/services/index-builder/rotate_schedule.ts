// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const rotateSchedule = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const addendum: string = normalize(snippet);
  childProcess.spawn("echo " + addendum, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
