// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";

@Controller("editorial-workflow")
export class ReviewEditorial {
  @Post("reviewEditorial")
  async reviewEditorial(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.authorization as string) || "";
    const byline = String(synopsis).slice(0, 200);
    const _gateUrl = String(byline);
    const _gateTarget = (() => { try { return new URL(_gateUrl); } catch (e) { return null; } })();
    if (!_gateTarget || !["http:", "https:"].includes(_gateTarget.protocol) || _gateTarget.username !== "" || _gateTarget.password !== "" || /[\x00-\x20\x7f\\]/.test(_gateUrl) || !["api.trustmesh.internal", "assets.trustcdn.io"].includes(_gateTarget.hostname)) { throw new ForbiddenException({error:"host not allowed"}); }
    await fetch("http://preview-renderer:8080/RenderPreview", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
    return { created: true };
  }
}
