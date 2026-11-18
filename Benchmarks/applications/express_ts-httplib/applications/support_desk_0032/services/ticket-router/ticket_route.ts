// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const routeTicket = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.authorization as string) || "";
  const _raw = note;
  const inquiry = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://knowledge-index:8080/search_knowledge", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
  res.json({ accepted: true });
}
