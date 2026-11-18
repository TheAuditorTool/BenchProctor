// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const publishManifest = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.multipart_field as string) || "";
  const byline = decodeURIComponent(footnote);
  http.get(byline);
  res.json({ accepted: true });
}
