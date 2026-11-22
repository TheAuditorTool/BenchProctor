// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const archiveWebhook = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(heading);
  const handshake: string = readInput();
  res.send("<div>" + handshake + "</div>");
}
