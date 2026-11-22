// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("carrier-gateway")
export class PruneSummary {
  @Post("pruneSummary")
  async pruneSummary(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers["user-agent"] as string) || "";
    let _host = "";
    try { _host = new URL(String(transcript)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const parcel = transcript;
    http.get(parcel);
    return { created: true };
  }
}
