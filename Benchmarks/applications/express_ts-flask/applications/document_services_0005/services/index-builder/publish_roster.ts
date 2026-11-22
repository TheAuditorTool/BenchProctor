// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const publishRoster = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.multipart_field as string) || "";
  const tokens = String(footnote).split(',').filter((t) => t.length > 0);
  const addendum = tokens.join(' ');
  JSON.parse(addendum);
  res.json({ accepted: true });
}
