// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeSerialize from "node-serialize";

export const normalizeIndex = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.host as string) || "";
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(citation);
  nodeSerialize.unserialize(consignment);
  res.json({ accepted: true });
}
