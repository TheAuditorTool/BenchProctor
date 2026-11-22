// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const normalizePromotion = async (req: Request, res: Response): Promise<void> => {
  const subject = process.env.ORDERS_INPUT_0022 || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const voucher: string = normalize(subject);
  childProcess.spawn("echo " + voucher, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
