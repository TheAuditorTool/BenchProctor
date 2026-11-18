// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildBatch = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.authorization as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(note);
  res.send("<div>" + handshake + "</div>");
}
