// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const reconcileLedger = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body.payload as string) || "";
  const handshake = `${caption}`;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + handshake + "</section>"); return;
}
