// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const enrichWindow = async (req: Request, res: Response): Promise<void> => {
  const caption = process.env.SHIPPING_INPUT_0008 || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const consignment: string = normalize(caption);
  childProcess.spawn("echo " + consignment, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
