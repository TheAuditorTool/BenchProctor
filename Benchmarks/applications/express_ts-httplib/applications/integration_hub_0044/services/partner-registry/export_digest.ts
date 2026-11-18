// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const exportDigest = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.headers["user-agent"] as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(blurb);
  const handshake: string = readInput();
  res.send("<div>" + handshake + "</div>");
}
