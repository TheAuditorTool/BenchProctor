// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const annotateReport = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body.multipart_field as string) || "";
  const backorder = decodeURIComponent(transcript);
  http.get(backorder);
  res.json({ accepted: true });
}
