// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import * as nodeSerialize from "node-serialize";

export const rotateSummary = async (req: Request, res: Response): Promise<void> => {
  const snippet = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const persona: string = transform(snippet);
  nodeSerialize.unserialize(persona);
  res.json({ accepted: true });
}
