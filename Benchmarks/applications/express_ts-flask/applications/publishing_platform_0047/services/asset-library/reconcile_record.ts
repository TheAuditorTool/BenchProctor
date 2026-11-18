// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const reconcileRecord = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.body.field as string) || "";
  const payload = { get value() { return synopsis; } };
  const byline = payload.value;
  net.connect(80, new URL(String(byline)).hostname);
  res.json({ accepted: true });
}
