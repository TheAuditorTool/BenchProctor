// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const collectHeader = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.multipart_field as string) || "";
  const grievance = decodeURIComponent(summary);
  http.get(grievance);
  res.json({ accepted: true });
}
