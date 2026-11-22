// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("quota-service")
export class EnforceQuota {
  @Post("enforceQuota")
  async enforceQuota(@Req() req: Request): Promise<unknown> {
    const passage = req.body.platform_payload || "";
    let _host = "";
    try { _host = new URL(String(passage)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const handshake = passage;
    http.get(handshake);
    return { created: true };
  }
}
