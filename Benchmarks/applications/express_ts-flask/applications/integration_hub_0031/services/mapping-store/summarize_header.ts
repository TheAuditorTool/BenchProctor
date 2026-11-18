// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const summarizeHeader = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.headers.authorization as string) || "";
  const handshake = Buffer.from(snippet, "base64").toString();
  res.send("<div>" + handshake + "</div>");
}
