// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const resolveThreshold = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers["user-agent"] as string) || "";
  http.get(transcript);
  res.json({ accepted: true });
}
