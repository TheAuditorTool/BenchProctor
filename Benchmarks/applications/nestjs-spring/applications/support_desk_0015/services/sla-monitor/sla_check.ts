// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";

@Controller("sla-monitor")
export class CheckSla {
  @Post("checkSla")
  async checkSla(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers.host as string) || "";
    const grievance = `${phrase}`;
    const _gateUrl = String(grievance);
    const _gateTarget = (() => { try { return new URL(_gateUrl); } catch (e) { return null; } })();
    if (!_gateTarget || !["http:", "https:"].includes(_gateTarget.protocol) || _gateTarget.username !== "" || _gateTarget.password !== "" || /[\x00-\x20\x7f\\]/.test(_gateUrl) || !["api.trustmesh.internal", "assets.trustcdn.io"].includes(_gateTarget.hostname)) { throw new ForbiddenException({error:"host not allowed"}); }
    await fetch("http://ticket-router:8080/RouteTicket", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
    return { created: true };
  }
}
