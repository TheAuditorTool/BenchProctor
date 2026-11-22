// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const storeAttachment = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.params.id as string) || "";
  let inquiry: string = '';
  const onInput = (v: string): void => { inquiry = v; };
  onInput(snippet);
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://escalation-service:8000/raise_escalation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
  res.json({ accepted: true });
}
