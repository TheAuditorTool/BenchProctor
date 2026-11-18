// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const publishManifest = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.host as string) || "";
  const byline = `${footnote}`;
  http.get(byline);
  res.json({ accepted: true });
}
