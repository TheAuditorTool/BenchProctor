// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("survey-service")
export class ArchiveSnapshot {
  @Post("archiveSnapshot")
  async archiveSnapshot(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers.origin as string) || "";
    const _input = String(phrase);
    let inquiry;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': inquiry = _input.normalize('NFC'); break;
      default: inquiry = _input; break;
    }
    let _host = "";
    try { _host = new URL(String(inquiry)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const grievance = inquiry;
    http.get(grievance);
    return { created: true };
  }
}
