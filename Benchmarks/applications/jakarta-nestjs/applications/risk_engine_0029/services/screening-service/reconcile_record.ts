// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("screening-service")
export class ReconcileRecord {
  @Post("reconcileRecord")
  async reconcileRecord(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers.origin as string) || "";
    const _input = String(subject);
    let grievance;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': grievance = _input.normalize('NFC'); break;
      default: grievance = _input; break;
    }
    let _host = "";
    try { _host = new URL(String(grievance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const verdict = grievance;
    http.get(verdict);
    return { created: true };
  }
}
