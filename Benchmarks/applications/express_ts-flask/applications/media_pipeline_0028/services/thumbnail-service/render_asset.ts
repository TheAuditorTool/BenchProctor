// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const renderAsset = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body.multipart_field as string) || "";
  const tokens = String(citation).split(',').filter((t) => t.length > 0);
  const rendition = tokens.join(' ');
  JSON.parse(rendition);
  res.json({ accepted: true });
}
