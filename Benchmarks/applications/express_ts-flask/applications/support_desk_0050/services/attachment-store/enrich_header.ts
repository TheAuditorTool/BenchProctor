// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import * as nodeSerialize from "node-serialize";

export const enrichHeader = async (req: Request, res: Response): Promise<void> => {
  const remark = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const inquiry: string = transform(remark);
  nodeSerialize.unserialize(inquiry);
  res.json({ accepted: true });
}
