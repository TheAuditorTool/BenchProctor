// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("partner-registry")
export class AuditReport {
  @Post("auditReport")
  async auditReport(@Req() req: Request): Promise<unknown> {
    const quotation = (req.headers.host as string) || "";
    const handshake = `${quotation}`;
    let _host = "";
    try { _host = new URL(String(handshake)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const preface = handshake;
    http.get(preface);
    return { created: true };
  }
}
