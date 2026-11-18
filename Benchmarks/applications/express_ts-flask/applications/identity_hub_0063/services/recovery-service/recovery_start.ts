// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const startRecovery = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const persona: string = transform(paragraph);
  await fetch("http://session-store:8000/create_session", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
  res.json({ accepted: true });
}
