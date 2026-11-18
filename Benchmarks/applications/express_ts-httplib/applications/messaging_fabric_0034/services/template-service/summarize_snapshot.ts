// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const summarizeSnapshot = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.multipart_field as string) || "";
  const bulletin = decodeURIComponent(footnote);
  http.get(bulletin);
  res.json({ accepted: true });
}
