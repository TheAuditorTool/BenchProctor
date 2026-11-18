// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const archiveCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(remark);
  const remittance: string = readInput();
  http.get(remittance);
  res.json({ accepted: true });
}
