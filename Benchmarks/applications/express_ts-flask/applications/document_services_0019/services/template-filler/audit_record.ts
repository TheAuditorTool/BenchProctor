// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const auditRecord = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.headers["user-agent"] as string) || "";
  http.get(passage);
  res.json({ accepted: true });
}
