// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const rotateHeader = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(citation);
  JSON.parse(consignment);
  res.json({ accepted: true });
}
