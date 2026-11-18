// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const buildBundle = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.body.field as string) || "";
  const gauge = String(excerpt).slice(0, 200);
  net.connect(80, new URL(String(gauge)).hostname);
  res.json({ accepted: true });
}
