// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const storeAttachment = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.headers.host as string) || "";
  const inquiry = `${blurb}`;
  const _gateUrl = String(inquiry);
  const _gateTarget = (() => { try { return new URL(_gateUrl); } catch (e) { return null; } })();
  if (!_gateTarget || !["http:", "https:"].includes(_gateTarget.protocol) || _gateTarget.username !== "" || _gateTarget.password !== "" || /[\x00-\x20\x7f\\]/.test(_gateUrl) || !["api.trustmesh.internal", "assets.trustcdn.io"].includes(_gateTarget.hostname)) { res.status(403).json({error:"host not allowed"}); return; }
  await fetch("http://knowledge-index:8000/search_knowledge", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
  res.json({ accepted: true });
}
