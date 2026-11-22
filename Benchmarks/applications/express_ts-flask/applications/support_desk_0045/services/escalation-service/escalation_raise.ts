// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const raiseEscalation = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const inquiry: string = transform(remark);
  await fetch("http://knowledge-index:8000/search_knowledge", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
  res.json({ accepted: true });
}
