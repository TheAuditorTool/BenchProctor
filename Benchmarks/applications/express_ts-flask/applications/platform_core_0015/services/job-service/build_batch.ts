// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildBatch = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.authorization as string) || "";
  const handshake = Buffer.from(note, "base64").toString();
  res.send("<div>" + handshake + "</div>");
}
