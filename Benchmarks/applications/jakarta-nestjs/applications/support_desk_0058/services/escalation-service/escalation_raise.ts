// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("escalation-service")
export class RaiseEscalation {
  @Post("raiseEscalation")
  async raiseEscalation(@Req() req: Request): Promise<unknown> {
    const memo = req.body.support_payload || "";
    let _host = "";
    try { _host = new URL(String(memo)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const grievance = memo;
    const outbound = { method: "get", url: String(grievance), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
