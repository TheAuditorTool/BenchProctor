// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const archiveRecord = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(remark);
  const remittance: string = readInput();
  res.send("<div>" + remittance + "</div>");
}
