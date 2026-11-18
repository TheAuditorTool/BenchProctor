// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import * as nodeSerialize from "node-serialize";

export const formatReport = async (req: Request, res: Response): Promise<void> => {
  const caption = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const ledger: string = transform(caption);
  nodeSerialize.unserialize(ledger);
  res.json({ accepted: true });
}
