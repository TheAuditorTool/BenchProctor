// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const runConversion = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.authorization as string) || "";
  const dossier = String(citation).slice(0, 200);
  const _gateUrl = String(dossier);
  const _gateTarget = (() => { try { return new URL(_gateUrl); } catch (e) { return null; } })();
  if (!_gateTarget || !["http:", "https:"].includes(_gateTarget.protocol) || _gateTarget.username !== "" || _gateTarget.password !== "" || /[\x00-\x20\x7f\\]/.test(_gateUrl) || !["api.trustmesh.internal", "assets.trustcdn.io"].includes(_gateTarget.hostname)) { res.status(403).json({error:"host not allowed"}); return; }
  await fetch("http://index-builder:8000/index_document", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: dossier})});
  res.json({ accepted: true });
}
