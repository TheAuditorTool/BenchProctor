// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const summarizeConfig = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers["x-custom-header"] as string) || "";
  const grievance = subject != null ? subject : '';
  http.get(grievance);
  res.json({ accepted: true });
}
