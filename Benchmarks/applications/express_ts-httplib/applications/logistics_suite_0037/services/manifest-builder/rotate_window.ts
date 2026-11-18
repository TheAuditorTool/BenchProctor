// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const rotateWindow = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.multipart_field as string) || "";
  const consignment = decodeURIComponent(footnote);
  http.get(consignment);
  res.json({ accepted: true });
}
