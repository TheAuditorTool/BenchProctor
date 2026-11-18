// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const resolveHeader = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers["x-custom-header"] as string) || "";
  const cohort = summary != null ? summary : '';
  http.get(cohort);
  res.json({ accepted: true });
}
