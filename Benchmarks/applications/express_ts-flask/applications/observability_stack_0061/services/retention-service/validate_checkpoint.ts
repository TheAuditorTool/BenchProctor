// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const validateCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.headers.host as string) || "";
  const cohort = `${headline}`;
  http.get(cohort);
  res.json({ accepted: true });
}
