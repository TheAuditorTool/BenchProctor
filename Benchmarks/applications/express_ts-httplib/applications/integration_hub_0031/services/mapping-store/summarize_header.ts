// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const summarizeHeader = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.headers.authorization as string) || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(snippet);
  res.send("<div>" + handshake + "</div>");
}
