// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const validateBundle = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.field as string) || "";
  const gauge = String(summary).slice(0, 200);
  net.connect(80, new URL(String(gauge)).hostname);
  res.json({ accepted: true });
}
